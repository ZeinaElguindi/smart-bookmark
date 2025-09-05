
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from urllib.parse import urlparse, quote

searchKeys = {
    "g": "https://www.google.com/search?q=",
    "yt": "https://www.youtube.com/results?search_query=",
    "gm": "https://www.google.com/maps/search/",
    "gh": "https://github.com/search?q=",
    "rd": "https://www.reddit.com/search/?q=",
    "am": "https://www.amazon.com/s?k=",
    "tw": "https://twitter.com/search?q=",
    "so": "https://stackoverflow.com/search?q=",
    # "gh": "https://github.com/",
    "lk": "https://www.linkedin.com/search/results/all/?keywords=",
    "learn": "https://learn.uwaterloo.ca/d2l/home/" 
}

def get_base_url(url: str):
    parsed_url = urlparse(url)

    return f"{parsed_url.scheme}://{parsed_url.netloc}/"

def get_learn_code(course_name):
    if course_name == "pd11":
        return "1162952"



def get_link(searchQuery):
    parts = searchQuery.split(" ", 1)
    cmd = parts[0]

    if cmd in searchKeys and (len(parts) == 1 or not parts[1].strip()):
        return get_base_url(searchKeys[cmd])

    if cmd not in searchKeys:
        cmd = "g"
        searchText = searchQuery
    else:
        searchText = parts[1].strip()

    if cmd == "learn":
        return searchKeys[cmd] + get_learn_code(searchText)

    if cmd == "gh":
        if "/" in searchText:
            return f"https://github.com/{searchText}"
        else:
            return f"https://github.com/search?q={quote(searchText)}"

    search = searchKeys[cmd] + quote(searchText)
    return search


app = FastAPI()

@app.get("/")
async def read_root(q: str):
    # return {"Hello": split(q)}
    return RedirectResponse(url=get_link(q))




