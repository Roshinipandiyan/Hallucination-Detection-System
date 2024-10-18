# 🧠 Hallucination Detection for Summaries 🚀

Welcome to **Hallucination Detection for Summaries**, a cool project designed to ensure summaries accurately reflect the original conversations! Whether you're dealing with multiple languages or complex dialogues, our tool detects hallucinations—parts of summaries that don't actually match the conversation—and helps keep things grounded in reality. 😎✨

---

## 📖 Table of Contents

- [Introduction](#introduction)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Team Contributions](#team-contributions)
- [Future Plans](#future-plans)

---

## 🌟 Introduction

Ever felt like your summary was a little too... creative? 😜 We’ve got you covered! This project tackles the problem of hallucinated summaries—those pesky lines that seem to appear out of nowhere, totally unlinked to the original conversation. Our solution analyzes conversations and summaries using machine learning techniques and flags any hallucinations, keeping everything in check.

---

## 🛠 Tech Stack

Here's the awesome tech behind this project:

- **Streamlit**: For that sleek, interactive UI 🎨
- **Pandas**: Data handling at its finest 🐼
- **Requests**: Seamless HTTP requests 💬
- **Flask**: Backend framework for smooth operations 🔥
- **Ollama**: For LLaMA model exploration 🦙
- **Emoji**: Because who doesn’t love emojis? 😁
- **Googletrans**: For translations that bridge languages 🌍
- **Torch**: Powering machine learning magic 🔥
- **Sentence-Transformers**: For handling semantic similarity in text 🧠

---

## 🧩 How It Works

1. **User Input**: Upload a CSV containing the conversation and its summary.
2. **Data Preprocessing**: Clean up the data by removing filler words, structure patterns, extra symbols, and whitespace. We even translate conversations if needed!
3. **ML Model**: Using the LLaMA model and sentence transformers, the tool compares the conversation and summary. It builds a contextual understanding of the conversation and checks if the summary faithfully represents it.
4. **Hallucination Scoring**: The model assigns a hallucination score based on discrepancies between the conversation and summary.
5. **Result**: If the summary deviates from the conversation, a hallucination is detected, and you're informed of the extent.

---

## ⚙️ Installation

Ready to dive in? Follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/hallucination-detection.git



Navigate to the project directory:

bash
Copy code
cd hallucination-detection
Install the required libraries:

bash
Copy code
pip install streamlit pandas requests flask ollama emoji googletrans torch sentence-transformers
Run the application:

bash
Copy code
streamlit run app.py
🚀 Usage
Upload your CSV file containing conversations and summaries.
Click to preprocess and analyze.
Get Results: The app will show whether hallucinations were detected and give you a confidence score!
💼 Team Contributions
Here’s the amazing team that made this project happen:

Arulpathi A: System Design, Data Preprocessing, Part-Phrase Model Exploration, Model Design & Development 🧠
Javagar M: System Design, Data Preprocessing, Part-Phrase Model Exploration, Model Design & Development 🧩
Roshini P: System Design, Frontend Design, Integration 🎨
Shiva Aravindha Samy A: System Design, LLaMA Model Exploration, Prompt Engineering & Testing 🚀
Vijayalakshmi P: System Design, LLaMA Model Exploration, Prompt Engineering & Testing, Integration 🔄
🌈 Future Plans
Expand Language Support: Improve translations for more languages.
Enhanced Visualization: Make hallucination detection more intuitive with detailed charts and visual breakdowns.
Refined Models: Continuously improve the model accuracy and hallucination detection.
Thanks for checking out our project! Give it a spin and let us know if your summaries are hallucination-free! ✨
