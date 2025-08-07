import streamlit as st
from data_parser import parse_file
from insight_engine import generate_summary, generate_summary_from_reviews
from ppt_generator import create_ppt
import time

st.set_page_config(page_title="AI Board Slide Generator", layout="centered")
st.title("📊 AI Board Meeting Slide Generator")
st.markdown("Upload your data file, and get an executive-ready PPT deck in seconds.")

uploaded_file = st.file_uploader("Upload Excel/CSV/PDF File", type=["xlsx", "csv", "pdf"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    if st.button("Generate Slides"):
        with st.spinner("Processing..."):
            try:
                metrics, df = parse_file(uploaded_file)

                st.info("🧠 Generating executive summary using Gemini...")
                start = time.time()
                try:
                    if "user_reviews" in metrics:
                        summary = generate_summary_from_reviews(metrics["user_reviews"])
                    else:
                        summary = generate_summary(metrics)

                    if time.time() - start > 15:
                        raise TimeoutError("Gemini took too long to respond.")

                except Exception as gen_error:
                    summary = f"⚠️ Summary could not be generated: {str(gen_error)}"

                ppt_path = create_ppt(metrics, summary, metrics.get("monthly_data", None))

                st.success("🎉 Slide deck created successfully!")
                with open(ppt_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Board Meeting Slides",
                        data=f,
                        file_name="Board_Meeting_Slides.pptx"
                    )

                st.subheader("Executive Summary")
                st.code(summary)

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
