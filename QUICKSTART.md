# Quick Start Guide - PDF Search Tool

## 🚀 Get Running in 2 Minutes

### Step 1: Install Dependencies (30 seconds)
```bash
pip install -r requirements.txt
```

### Step 2: Run the App (10 seconds)
```bash
streamlit run pdf_search_app.py
```

Your browser will open automatically. If not, visit: **http://localhost:8501**

---

## 💡 First Use Example

1. **Prepare your PDFs**
   - Put all PDF files in a folder
   - Compress folder to ZIP (right-click → Send to → Compressed folder)

2. **Upload ZIP**
   - Click "Upload ZIP file containing PDFs" in the left sidebar
   - Select your ZIP file

3. **Search**
   - Click the "Search" tab
   - Type what you're looking for (e.g., "invoice", "date", "total")
   - Click Enter or wait for results

4. **Download**
   - Click "📥 Download" button next to matching PDFs

---

## 🎯 Example Searches

**Business Documents:**
- "invoice number"
- "total amount"
- "payment date"

**Reports:**
- "summary"
- "conclusion"
- "2024"

**Contracts:**
- "effective date"
- "signature"
- "terms"

---

## ❓ FAQ

**Q: Do I need an API key?**
A: NO! Everything runs locally on your computer.

**Q: Is my data secure?**
A: YES! Files never leave your machine. All processing is local.

**Q: What file types are supported?**
A: PDF files in ZIP archives. Other formats coming soon!

**Q: Can I search multiple ZIPs?**
A: Upload one at a time. Start fresh for a new ZIP.

**Q: How large can my ZIP be?**
A: Works great with 1GB+ archives, but search speed depends on PDF complexity.

---

## 🆘 Having Issues?

**"ModuleNotFoundError: No module named 'streamlit'"**
```bash
pip install streamlit==1.39.0
```

**"ModuleNotFoundError: No module named 'pypdf'"**
```bash
pip install pypdf==4.0.1
```

**The app won't start**
- Ensure Python 3.8+ is installed: `python --version`
- Run: `pip install -r requirements.txt` again
- Restart your terminal

**Searches are slow**
- Large PDFs take longer to search
- This is normal behavior
- Try shorter search terms

---

## 📞 Need Help?

- Check the main **README.md** for detailed documentation
- Review the **Troubleshooting** section in README.md
- Ensure all dependencies are installed correctly

---

**Happy searching! 🔍**
