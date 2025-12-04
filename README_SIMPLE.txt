SIMPLE SETUP GUIDE (FOR NON-TECH USERS)

1) This folder contains:
   - main.py
   - whatsapp.py
   - blogger.py
   - helpers.py
   - requirements.txt

2) This automation will:
   ✔ Send WhatsApp messages automatically
   ✔ Post blog articles on Blogger automatically
   ✔ Run on schedule multiple times daily

3) GitHub Secrets you must add:
   - WHATSAPP_PHONE_ID
   - WHATSAPP_PERMANENT_TOKEN
   - WHATSAPP_TO_NUMBER
   - BLOGGER_BLOG_ID

4) token.json (for Blogger):
   - Generate using Google OAuth via Blogger API Quickstart
   - Place token.json in project root when running locally
   - Do NOT upload token.json to GitHub

5) How to run the automation:
   - Go to GitHub Actions tab
   - Trigger manually OR wait for scheduled times

6) Important:
   - This system runs 100% online on GitHub servers
   - Your PC doesn't need to be ON
