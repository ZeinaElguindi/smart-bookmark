# 🔖 Smart Bookmark

A tiny FastAPI app that turns **aliases → searches**.  
Example: `g cats` → Google, `yt lo-fi` → YouTube, `gm ramen` → Maps 🍜

---

## 🚀 Quick Start

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open in your browser:

```
http://localhost:8000/?q=g matrix calculus
```

---

## 🌐 Add as Search Engine

Use your deployed URL (for example):

```
https://smart-bookmark.vercel.app/?q=%s
```

### Chrome
1. Go to **Settings → Search engine → Manage search engines**
2. Click **Add** and fill in:
   - **Name:** Smart Bookmark  
   - **Keyword:** `sb` (or leave blank if you’ll set it as default)  
   - **URL:** `https://smart-bookmark.vercel.app/?q=%s`
3. Click the three dots → **Make default** ✅

### Safari
Safari doesn’t support adding custom search engines directly.  
Options:  
- Use a Safari extension like **Add Custom Search Engine**  
- Or create a bookmark with this URL format:  
  ```
  https://smart-bookmark.vercel.app/?q=%s
  ```

### Firefox
1. Open **Preferences → Search → Add shortcut**
2. Fill in:
   - **Keyword:** `sb`  
   - **URL:** `https://smart-bookmark.vercel.app/?q=%s`

---

## 🧩 Supported Aliases

| Alias | Destination 🌐 |
|-------|----------------|
| `g`   | Google Search 🔍 |
| `yt`  | YouTube 🎬 |
| `gm`  | Google Maps 🗺️ |
| `gh`  | GitHub 🐙 |
| `rd`  | Reddit 👽 |
| `am`  | Amazon 📦 |
| `tw`  | Twitter/X 🐦 |
| `so`  | Stack Overflow 💡 |

---

## 🔧 Add Your Own Commands

Edit the dictionary in **`main.py`**:

```python
searchKeys["imdb"] = "https://www.imdb.com/find/?q="
searchKeys["am"] = searchKeys["amazon"] = "https://www.amazon.com/s?k="
```

Redeploy → Done 🎉

---

## 💡 Notes

- First word = alias (`g`, `yt`, `gm`, …)  
- Rest = your query  
- Redirects instantly, no tracking ✨  

---

## ❓ FAQ

**Q: Can I add new commands without editing the code?**  
A: Not yet. Right now, you add commands by editing `main.py` and redeploying.  

**Q: Does this collect or track searches?**  
A: No. It just redirects to the target site.  

**Q: Do I have to make it my default search engine?**  
A: Nope — you can set it up as a keyword (`sb`) and only use it when you want.  

**Q: Can I run it locally instead of deploying?**  
A: Yes! Just run `uvicorn main:app --reload` and point your browser to `http://localhost:8000/?q=g test`.  
