import streamlit as st
from transformers import pipeline
import PyPDF2

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

model = load_model()

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def generate_flashcards(text, subject):
    prompt = (
        f"You are a helpful education assistant.\n"
        f"Generate 10-15 flashcards for the subject: {subject}.\n"
        f"For each flashcard, follow this format:\n"
        f"Q: [question]\nA: [answer]\n\n"
        f"Educational content:\n{text[:2000]}\n"
    )
    result = model(prompt, max_length=1024, do_sample=False)[0]["generated_text"]
    return result

def format_flashcards(raw_output):
    flashcards = []
    for line in raw_output.strip().split("\n"):
        line = line.strip()
        if line.startswith("Q:") or line.startswith("A:"):
            flashcards.append(line)
    return flashcards

st.title("📚 Hugging Face Flashcard Generator")

uploaded_file = st.file_uploader("Upload a PDF (.pdf)", type="pdf")
raw_text_input = st.text_area("Or paste your educational text here:")
subject = st.selectbox("Select subject type:", ["General", "Biology", "History", "Computer Science"])

if st.button("Generate Flashcards"):
    with st.spinner("Generating... Please wait..."):
        content = ""
        if uploaded_file:
            content = extract_text_from_pdf(uploaded_file)
        elif raw_text_input:
            content = raw_text_input

        if not content.strip():
            st.error("Please upload a PDF or paste some content.")
        else:
            output = generate_flashcards(content, subject)
            flashcards = format_flashcards(output)

            if flashcards:
                st.success("Generated Flashcards:")
                for i in range(0, len(flashcards), 2):
                    if i + 1 < len(flashcards):
                        st.markdown(f"**{flashcards[i]}**\n{flashcards[i+1]}")
                st.download_button("Download Flashcards (.txt)", data='\n'.join(flashcards), file_name="flashcards.txt")
            else:
                st.warning("⚠️ No flashcards detected. Showing raw model output:")
                st.code(output)
