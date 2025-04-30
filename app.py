import streamlit as st
from langchain_core.prompts import PromptTemplate
from src.utils import extract_text_from_pdf, ask_gemini, fetch_linkedin_jobs


# Streamlit App Configuration
st.set_page_config(page_title="AI Resume Analyzer + Job Finder", layout='wide')

# Branding Header with Logo and Tagline
col1, col2 = st.columns([1, 10])
with col1:
    st.image("images/logo.png", width=60)  # Replace with URL if hosted online
with col2:
    st.markdown("<h3 style='margin-bottom:0;'>AI Resume Analyzer & Career Growth Advisor</h3>", unsafe_allow_html=True)

st.markdown("Upload your Resume and get career insights + live job recommendations from Linkedin:")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        # Call Gemini for different tasks
        with st.spinner("Summarizing Resume..."):
            prompt_summary = PromptTemplate(
                input_variables=["resume_text"],  
                template="Summarize this resume highlighting skills, education, and experience:\n\n{resume_text}"
                )
            summary = ask_gemini(prompt=prompt_summary, text_input={"resume_text": resume_text})

        with st.spinner("Finding Skill Gaps..."):
            prompt_gaps = PromptTemplate(
                input_variables=["resume_text"],  
                template="Analyze this resume and highlight missing skills, certifications, or experiences needed for better job opportunities:\n\n{resume_text}"
                )
            gaps = ask_gemini(prompt=prompt_gaps, text_input={"resume_text": resume_text})

        with st.spinner("Creating Future Roadmap..."):
            prompt_roadmap = PromptTemplate(
                input_variables=["resume_text"],  
                template="Based on this resume, suggest a future roadmap to improve this person's career projects (skills to learn, certifications needed, industry exposure):\n\n{resume_text}"
                )
            roadmap = ask_gemini(prompt=prompt_roadmap, text_input={"resume_text": resume_text})

        # Display nicely formatted results
        st.markdown("___")
        st.header("Resume Summary")
        st.markdown(
            f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color: white'>{summary['text']}</div>",
            unsafe_allow_html=True
        )

        st.markdown("___")
        st.header("Skill Gaps & Missing Areas")
        st.markdown(
            f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color: white'>{gaps['text']}</div>",
            unsafe_allow_html=True
        )

        st.markdown("___")
        st.header("Future Roadmap & Preparation Strategy")
        st.markdown(
            f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size: 16px; color: white'>{roadmap['text']}</div>",
            unsafe_allow_html=True
        )


        st.success("Analysis Completed Successfully.")

        # Button to Fetch Jobs
        if st.button("Fetch Matching Jobs Now"):
            with st.spinner("Extracting best keywords from resume..."):
                prompt_roadmap = PromptTemplate(
                input_variables=["summary"],  
                template="Based on this resume summary, suggest the best job titles/keywords for searching jobs. Give a comma-separated list only, no explanation.\n\nSummary:\n{summary}"
                )
                keywords = ask_gemini(prompt=prompt_roadmap, text_input={"summary": summary['text']})
                search_keywords_clean = keywords.get("text", "").replace("\n", "").strip()


                st.success(f"Extracted Job Keywords: {search_keywords_clean}")

                # Fetch Jobs
                with st.spinner("Fetching Jobs from LinkedIn..."):
                    linkedin_jobs = fetch_linkedin_jobs(search_query=search_keywords_clean, rows=3)

                st.markdown('---')
                st.header("Top LinkedIn Jobs (SRI LANKA)")

                if linkedin_jobs:
                    for job in linkedin_jobs:
                        st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                        st.markdown(f"{job.get('location')}")
                        st.markdown(f"Job Link:{job.get('jobUrl')}")
                        st.markdown(f"Apply:{job.get('applyUrl')}")
                        # st.markdown(f"[View Job]({job})")
                        st.markdown("---")
                else:
                    st.warning("No LinkedIn jobs found.")

                st.markdown('---')

st.markdown(
    "<div style='text-align: center; color: gray;'>🚀 Product by GD</div>",
    unsafe_allow_html=True
)

    