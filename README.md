# PDF Search Tool - Streamlit Application

A professional web application to search PDF files within ZIP archives. Extract, search, and download specific PDFs based on your queries.

## 🎯 Features

- **ZIP File Upload**: Upload ZIP files containing PDF documents
- **Full-Text Search**: Search across all PDFs in the archive
- **Smart Context Display**: View text snippets around matched content
- **File Statistics**: View file count, total size, and page information
- **Direct Download**: Download PDF files directly from results
- **Case-Sensitive Search**: Optional case-sensitive search option
- **Real-time Processing**: Fast extraction and searching

## ⚙️ Requirements

**NO API KEY REQUIRED!** This application uses only open-source libraries.

### Dependencies
- Python 3.8+
- streamlit
- pypdf

## 🚀 Installation & Setup

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run pdf_search_app.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 How to Use

### Step 1: Upload ZIP File
- Click the upload button in the left sidebar
- Select a ZIP file containing PDF documents
- The app will extract and process all PDFs automatically

### Step 2: Search
- Go to the "🔍 Search" tab
- Enter your search term in the text field
- Optionally enable "Case sensitive" search
- The app will search all PDFs and display results

### Step 3: View Results
- Results show:
  - **Filename** - Name of the PDF file
  - **Match Count** - Number of times the search term appears
  - **File Size** - Size of the PDF in KB
  - **Context** - Text snippets showing the match in context

### Step 4: Download
- Click the "📥 Download" button next to any result
- The PDF file will be downloaded to your computer

### File Overview Tab
- View statistics about all files in your ZIP
- See total size, page count, and file listing
- Useful for understanding your document collection

## 📝 Example Workflow

1. **Create a ZIP file** with PDFs:
   ```
   mydocuments.zip
   ├── report1.pdf
   ├── report2.pdf
   └── invoice.pdf
   ```

2. **Upload the ZIP** to the application

3. **Search for content**:
   - Example: "invoice number" or "Q3 2024"
   - Results show which PDFs contain this text

4. **Download matches** directly from results

## 🔍 Search Tips

- **Case Insensitive** (Default): Finds "Invoice", "invoice", "INVOICE"
- **Case Sensitive**: Searches for exact case matches
- **Phrases**: Search for multi-word phrases
- **Special Characters**: Supported in search terms
- **Partial Words**: Finds partial matches within text

## 📊 Performance

- **Small Archives** (< 50MB): Processes instantly
- **Medium Archives** (50-500MB): Processes within 1-2 seconds
- **Large Archives** (> 500MB): May take several seconds

> Note: Processing time depends on PDF complexity and text extraction difficulty

## 🛡️ Security & Privacy

- ✅ All processing happens **locally** on your machine
- ✅ Files are **not uploaded** to any server
- ✅ No external API calls
- ✅ Temporary files are cleaned up automatically
- ✅ No data collection or tracking

## 🐛 Troubleshooting

### Issue: "Error reading PDF"
**Solution**: Some PDFs may have encoding issues. The app will skip problematic files and continue searching.

### Issue: Slow search on large files
**Solution**: This is normal for large PDF archives. Streamlit is re-rendering as it processes.

### Issue: ZIP extraction fails
**Solution**: Ensure the ZIP file is not corrupted. Try re-zipping the PDFs.

### Issue: No results found
**Solution**: 
- Try a different search term
- Check the "File Overview" tab to see what files are included
- Verify the search term exists in your PDFs

## 📦 File Structure

```
.
├── pdf_search_app.py          # Main Streamlit application
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Advanced Usage

### Modify Search Behavior
Edit the `search_pdfs()` function in `pdf_search_app.py` to:
- Change match context length (currently 100 chars)
- Limit number of matches displayed (currently 10)
- Add regex pattern matching

### Extend Functionality
The app can be extended to support:
- Different file formats (DOCX, XLSX, TXT)
- PDF text extraction improvements
- Export search results as CSV
- Batch search operations

## 📄 API & Library Info

- **pypdf**: Python library for reading PDF files
  - License: BSD 3-Clause
  - Handles text extraction, page counting, file operations

- **streamlit**: Open-source Python framework for data apps
  - License: Apache 2.0
  - Creates interactive web UI without frontend coding

## ✨ What's Included

- ✅ ZIP file processing
- ✅ Multi-page PDF text extraction
- ✅ Case-sensitive/insensitive search
- ✅ Context display around matches
- ✅ File statistics
- ✅ Direct PDF downloads
- ✅ Professional UI with tabs
- ✅ No external API calls
- ✅ No API keys required
- ✅ Local-only processing

## 📝 Version

**v1.0** - Initial Release

## 📞 Support

For issues with:
- **Streamlit**: https://docs.streamlit.io/
- **pypdf**: https://github.com/py-pdf/pypdf

## 📄 License

Open source - Feel free to modify and distribute

---

**Built with ❤️ for efficient document searching**
