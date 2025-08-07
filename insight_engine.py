import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(metrics):
    prompt = f"""
    You're a business analyst creating an executive summary based on the following metrics:
    - Total Revenue: ₹{metrics['total_revenue']}
    - Total Cost: ₹{metrics['total_cost']}
    - Average Churn Rate: {metrics['avg_churn']}%
    - Active Regions: {', '.join(metrics['regions'])}

    Write a clear, professional summary for a board slide. Mention 1–2 insights and 1 strategic recommendation.
    """

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
