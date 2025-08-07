import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")  # Ensure correct model name

def generate_summary(metrics):
    prompt = f"""
    You're a business analyst preparing a short executive summary for a board slide. 
    Based on the metrics below, write a **clear, concise, professional summary under 80 words.**
    
    - Total Revenue: ₹{metrics['total_revenue']}
    - Total Cost: ₹{metrics['total_cost']}
    - Average Churn Rate: {metrics['avg_churn']}%
    - Active Regions: {', '.join(metrics['regions'])}
    
    Mention 1–2 insights and 1 recommendation.
    """
    response = model.generate_content(prompt)
    return response.text.strip()[:600]  # Truncate if needed

def generate_summary_from_reviews(review_text):
    prompt = f"""
    You're analyzing customer feedback from the following reviews:

    {review_text[:2000]}

    Provide a **short and clear summary under 80 words** suitable for an executive slide.
    Highlight key sentiments and 1 major recommendation.
    """
    response = model.generate_content(prompt)
    return response.text.strip()[:600]  # Truncate if needed
