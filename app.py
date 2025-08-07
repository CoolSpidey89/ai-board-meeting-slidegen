import streamlit as st
from data_parser import parse_excel
from insight_engine import generate_summary
from ppt_generator import create_ppt

st.set_page_config(page_title="AI Board Slide Generator", layout="centered")

st.title("📊 AI Board Meeting Slide Generator")
st.markdown("Upload your Excel file, and get an executive-ready PPT deck in seconds.")

uploaded_file = st.file_uploader("Upload Q2 Financial Excel File (.xlsx)", type=["xlsx"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    if st.button("Generate Slides"):
        with st.spinner("Processing..."):
            try:
                metrics, df = parse_excel(uploaded_file)
                summary = generate_summary(metrics)
                ppt_path = create_ppt(metrics, summary, metrics["monthly_data"])

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
