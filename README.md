# LLM-Powered-Flashcard-Generator-
A lightweight Streamlit application that uses Hugging Face's flan-t5-base model to generate flashcards (Q\&amp;A format) from educational content such as PDFs or raw text input. put everything  
## Features

* Upload PDF files or paste raw educational text.
* Auto-generates 10-15 flashcards with questions and answers.
* Option to download flashcards as a .txt file.
* Subject-based generation: General, Biology, History, or CS.

## Tech Stack

* **Frontend**: Streamlit
* **LLM**: google/flan-t5-base from Hugging Face Transformers
* **PDF Handling**: PyPDF2
* **Language**: Python

## ⚡ Installation

1. **Clone the repo:**

git clone https://github.com/yourusername/llm-flashcard-generator
cd llm-flashcard-generator


2. **Set up virtual environment:**

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate


3. **Install dependencies:**

pip install -r requirements.txt


4. **Add API key** (optional if needed):
   Create a .env file:

env
HF_API_KEY=your-huggingface-api-key


5. **Run the app:**

streamlit run app.py

##  Usage

* Upload a .pdf file **OR** paste educational content.
* Choose a subject category.
* Click **"Generate Flashcards"**.
* View and download the generated flashcards.

## Author

**Nikita Sinha**
\[sinhanikita275@gmail.com]
