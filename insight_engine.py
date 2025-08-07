import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")


def generate_summary(metrics):
    prompt = f"""
    You're a business analyst creating an executive summary based on the following metrics:
    - Total Revenue: ₹{metrics['total_revenue']}
    - Total Cost: ₹{metrics['total_cost']}
    - Average Churn Rate: {metrics['avg_churn']}%
    - Active Regions: {', '.join(metrics['regions'][:5])}{' and more' if len(metrics['regions']) > 5 else ''}

    Write a clear, professional summary for a board slide. Mention 1–2 insights and 1 strategic recommendation.
    """

    response = model.generate_content(prompt)
    return response.text.strip()

def generate_summary_from_reviews(review_text):
    prompt = f"""
    The following are customer/user reviews collected over the last quarter:

    {review_text[:8000]}

    Summarize the major sentiments, highlight common issues, and recommend one improvement strategy.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
