from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate


app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Cool Ass Post"},
    2: {"title": "Second Drop", "content": "Still Cool, Still Ass"},
    3: {"title": "Late Night Thoughts", "content": "Code works better after midnight"},
    4: {"title": "Debug Diaries", "content": "It was a missing comma. Again."},
    5: {"title": "Hot Take", "content": "Async is great until you block it"},
    6: {"title": "Production Story", "content": "Worked in dev. Broke in prod."},
    7: {"title": "API Life", "content": "Just one more endpoint"},
    8: {"title": "Coffee Powered", "content": "This app runs on caffeine"},
    9: {"title": "Refactor Day", "content": "Nothing changed. Everything broke."},
    10: {"title": "Ship It", "content": "We'll fix it later"}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)


@app.post("/posts")
def create_posts(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


