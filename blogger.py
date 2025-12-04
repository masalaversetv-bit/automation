# blogger.py
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BLOG_ID = os.getenv("BLOGGER_BLOG_ID")

def post_to_blogger(title, html_content):
    # token.json must be included in the repo root (NOT uploaded to GitHub)
    creds = Credentials.from_authorized_user_file("token.json")
    service = build('blogger', 'v3', credentials=creds)

    body = {
        "kind": "blogger#post",
        "title": title,
        "content": html_content
    }

    post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    return post.get("url")
