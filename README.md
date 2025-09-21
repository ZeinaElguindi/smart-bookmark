🔖 Smart Bookmark

A FastAPI app that turns aliases → searches.
Example: g cats → Google, yt lo-fi → YouTube, gm ramen → Maps 🍜.


🚀 Quick Start
pip install fastapi uvicorn
uvicorn main:app --reload


Then try:
http://localhost:8000/?q=g matrix calculus


🌐 Add as Search Engine

Use your deployed URL (e.g. https://smart-bookmark.vercel.app/?q=%s).

Chrome / Edge / Brave → Settings → Search engine → Add → make default ✅

Firefox → Preferences → Search → Add keyword (e.g. sb) → URL with %s

Now just type g eigenvalues or yt lo-fi.

🧩 Examples

g eigenvalues → Google

yt transformers lecture → YouTube

gh fastapi → GitHub

so python f-string → Stack Overflow

🔧 Add Your Own Commands

Edit the dictionary in main.py:

searchKeys["imdb"] = "https://www.imdb.com/find/?q="
searchKeys["am"] = searchKeys["amazon"] = "https://www.amazon.com/s?k="


Redeploy → Done 🎉
