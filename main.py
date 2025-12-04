# main.py
import os
from datetime import datetime
from whatsapp import send_whatsapp_text
from blogger import post_to_blogger

def generate_market_report():
    # Placeholder market update — tum baad me apna logic daal sakte ho
    now = datetime.now().strftime("%d %b %Y %I:%M %p")
    text = f"""
Market Update — {now}

📈 Nifty Key Levels:
• Support: 22050
• Resistance: 22300
• Trend: Sideways to bullish

🔥 Breakout Stocks:
• Stock A
• Stock B
• Stock C

📰 Important News:
• Market in consolidation
• FII/DII flows stable

(This is a sample — replace with your own analysis.)
"""
    return text.strip()

def run():
    report = generate_market_report()

    # 1 — Send WhatsApp Update
    try:
        send_whatsapp_text(report)
        print("WhatsApp Sent Successfully!")
    except Exception as e:
        print("WhatsApp Failed:", e)

    # 2 — Publish Blog Post
    blog_title = f"Market Update — {datetime.now().strftime('%d %b %Y %I:%M %p')}"
    blog_body = report.replace("\n", "<br>")

    try:
        blog_url = post_to_blogger(blog_title, blog_body)
        print("Blogger URL:", blog_url)
        # 3 — Send WhatsApp confirmation
        send_whatsapp_text(f"Blog Posted Successfully!\n🔗 {blog_url}")

    except Exception as e:
        print("Blogger failed:", e)
        send_whatsapp_text(f"Blogger post failed ❌\nReason: {str(e)}")


if __name__ == "__main__":
    run()
