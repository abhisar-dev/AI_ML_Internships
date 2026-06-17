import streamlit as st
from pypdf import PdfReader

st.title("AI Resume Analyzer")

skills_db = [
    "python",
    "java",
    "machine learning",
    "software development",
    "problem solving",
    "ms office",
    "internet research",
    "teamwork",
    "ai",
    "artificial intelligence",
    "git",
    "github",
    "sql"
]
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("Resume Text")
    st.text_area("", text, height=200)

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No skills detected")
        # ATS Score
total_skills = len(skills_db)
matched_skills = len(found_skills)

ats_score = int((matched_skills / total_skills) * 100)

st.subheader("ATS Score")
st.progress(ats_score)

if ats_score >= 80:
    st.success(f"Excellent ATS Score: {ats_score}/100")
elif ats_score >= 50:
    st.warning(f"Average ATS Score: {ats_score}/100")
else:
    st.error(f"Low ATS Score: {ats_score}/100")
st.subheader("Resume Feedback")

if ats_score >= 80:
    st.success("Resume demonstrates strong technical skill coverage and is well aligned with industry expectations.")
elif ats_score >= 60:
    st.info("Resume shows a solid foundation of technical skills with opportunities for further enhancement.")
elif ats_score >= 40:
    st.warning("Resume contains some relevant skills but would benefit from additional technical competencies.")
else:
    st.error("Resume requires significant improvement in technical skill representation.")
    st.subheader("Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)
if job_description:

    matched_skills = []

    for skill in skills_db:
        if (
            skill.lower() in text.lower()
            and skill.lower() in job_description.lower()
        ):
            matched_skills.append(skill)

    match_score = int(
        (len(matched_skills) / len(skills_db)) * 100
    )

    st.subheader("Resume Match Score")
    st.progress(match_score)

    st.write(f"Match Score: {match_score}/100")

    st.subheader("Matched Skills")

    if matched_skills:
        for skill in matched_skills:
            st.write(skill)
    else:
        st.write("No matching skills found.")