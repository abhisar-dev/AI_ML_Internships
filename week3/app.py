import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="AI Study Companion Pro")

st.title("AI Study Companion Pro")
st.write("Upload study material and generate learning insights.")

uploaded_file = st.file_uploader(
    "Upload PDF Notes",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("Document Statistics")

    words = len(text.split())
    st.subheader("Study Readiness Score")

    score = min(words // 50, 100)

    st.progress(score)

    st.write(f"Score: {score}/100")

    st.write(f"Total Words: {words}")

    st.subheader("Document Preview")

    st.text_area(
        "Extracted Text",
        text[:3000],
        height=300
    )

    st.subheader("Quick Summary")
    sentences = text.split(".")
    summary = ".".join(sentences[:5])
    st.write(summary)
    st.subheader("Important Topics")

    all_words = text.split()

    filtered_words = []

    for word in all_words:
        if len(word) > 6:
            filtered_words.append(word)

    topics = list(set(filtered_words))

    for topic in topics[:15]:
        st.write(topic)
        st.subheader("Practice Quiz")

    for i, topic in enumerate(topics[:5], 1):
        st.write(f"{i}. What is {topic}?")
        st.subheader("Practice Questions")

    for topic in topics[:5]:
        st.write(f"• Explain {topic}")
        st.subheader("Flashcards")

    for topic in topics[:5]:
        st.info(topic)