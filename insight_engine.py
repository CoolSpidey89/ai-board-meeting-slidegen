import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_summary(metrics):
    prompt = f"""
    You're a business analyst creating an executive summary based on the following metrics:
    - Total Revenue: ₹{metrics['total_revenue']}
    - Total Cost: ₹{metrics['total_cost']}
    - Average Churn Rate: {metrics['avg_churn']}%
    - Active Regions: {', '.join(metrics['regions'])}

    Write a clear, professional summary for a board slide. Mention 1–2 insights and 1 strategic recommendation.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
