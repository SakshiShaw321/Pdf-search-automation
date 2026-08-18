import streamlit as st
import zipfile
import os
import shutil
from pathlib import Path
from pypdf import PdfReader
import re

# Page configuration
st.set_page_config(
    page_title="PDF Search Tool",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📄 PDF Search Tool")
st.markdown("---")

# Initialize session state
if "uploaded_zip" not in st.session_state:
    st.session_state.uploaded_zip = None
if "extracted_pdfs" not in st.session_state:
    st.session_state.extracted_pdfs = {}
if "search_results" not in st.session_state:
    st.session_state.search_results = None

# Sidebar - File Upload
st.sidebar.header("Upload & Configure")
uploaded_file = st.sidebar.file_uploader(
    "Upload ZIP file containing PDFs",
    type="zip",
    help="Select a ZIP file that contains PDF documents"
)

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    """Extract all text from a PDF file"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# Process uploaded zip file
def process_zip_file(uploaded_file):
    """Extract and process all PDFs from zip file"""
    temp_dir = Path("temp_pdfs")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir(exist_ok=True)

    # Extract zip file
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    # Find all PDFs and extract text
    pdf_data = {}
    for pdf_path in temp_dir.rglob("*.pdf"):
        text = extract_text_from_pdf(str(pdf_path))
        pdf_data[pdf_path.name] = {
            "path": str(pdf_path),
            "text": text,
            "size": os.path.getsize(str(pdf_path))
        }

    return pdf_data

# Search function
def search_pdfs(query, pdf_data, case_sensitive=False):
    """Search for query in all PDFs"""
    results = {}
    flags = 0 if case_sensitive else re.IGNORECASE
    pattern = re.compile(re.escape(query), flags)

    for filename, data in pdf_data.items():
        matches = pattern.finditer(data["text"])
        matches_list = list(matches)

        if matches_list:
            # Get context around matches
            context_list = []
            for match in matches_list[:10]:  # Limit to first 10 matches
                start = max(0, match.start() - 100)
                end = min(len(data["text"]), match.end() + 100)
                context = data["text"][start:end].replace("\n", " ")
                context_list.append(f"...{context}...")

            results[filename] = {
                "match_count": len(matches_list),
                "contexts": context_list,
                "size": data["size"]
            }

    return results

# Main application logic
if uploaded_file is not None:
    st.sidebar.success("✅ ZIP file uploaded successfully!")

    if st.session_state.extracted_pdfs == {} or st.session_state.uploaded_zip != uploaded_file.name:
        with st.spinner("Processing ZIP file..."):
            st.session_state.extracted_pdfs = process_zip_file(uploaded_file)
            st.session_state.uploaded_zip = uploaded_file.name

        st.sidebar.success(f"Found {len(st.session_state.extracted_pdfs)} PDF(s)")

    # Main tabs
    tab1, tab2 = st.tabs(["🔍 Search", "📊 File Overview"])

    with tab1:
        st.header("Search PDF Content")

        col1, col2 = st.columns([3, 1])

        with col1:
            search_query = st.text_input(
                "What do you want to find?",
                placeholder="Enter search term...",
                help="Type keywords, phrases, or terms to search in PDFs"
            )

        with col2:
            case_sensitive = st.checkbox("Case sensitive")

        if search_query:
            with st.spinner("Searching..."):
                results = search_pdfs(search_query, st.session_state.extracted_pdfs, case_sensitive)
                st.session_state.search_results = results

            if results:
                st.success(f"✅ Found in {len(results)} file(s)")
                st.markdown("---")

                for filename, data in results.items():
                    with st.container(border=True):
                        col1, col2 = st.columns([4, 1])

                        with col1:
                            st.subheader(f"📄 {filename}")
                            st.write(f"**Matches found:** {data['match_count']}")
                            st.write(f"**File size:** {data['size'] / 1024:.2f} KB")

                            with st.expander("View context"):
                                for i, context in enumerate(data['contexts'][:5], 1):
                                    st.caption(f"**Match {i}:**")
                                    st.text(context)

                        with col2:
                            # Download button
                            pdf_path = st.session_state.extracted_pdfs[filename]["path"]
                            with open(pdf_path, "rb") as f:
                                st.download_button(
                                    label="📥 Download",
                                    data=f.read(),
                                    file_name=filename,
                                    mime="application/pdf",
                                    use_container_width=True
                                )
            else:
                st.warning(f"❌ No results found for '{search_query}'")
        else:
            st.info("👆 Enter a search term above to get started")

    with tab2:
        st.header("File Overview")

        if st.session_state.extracted_pdfs:
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Files", len(st.session_state.extracted_pdfs))

            with col2:
                total_size = sum(data["size"] for data in st.session_state.extracted_pdfs.values())
                st.metric("Total Size", f"{total_size / (1024*1024):.2f} MB")

            with col3:
                total_pages = sum(
                    len(PdfReader(data["path"]).pages)
                    for data in st.session_state.extracted_pdfs.values()
                )
                st.metric("Total Pages", total_pages)

            st.markdown("---")
            st.subheader("Files in ZIP")

            file_data = []
            for filename, data in st.session_state.extracted_pdfs.items():
                try:
                    pages = len(PdfReader(data["path"]).pages)
                except:
                    pages = "N/A"

                file_data.append({
                    "Filename": filename,
                    "Size (KB)": f"{data['size'] / 1024:.2f}",
                    "Pages": pages
                })

            st.dataframe(file_data, use_container_width=True)
else:
    st.info("👈 Upload a ZIP file containing PDFs to get started")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
    <small>Developed by Sakshi Shaw (RML034549) | Streamlit PDF Search Tool </small>
    </div>
    """,
    unsafe_allow_html=True
)
