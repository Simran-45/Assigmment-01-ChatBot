# 🤖 Streamlit + Groq AI Chatbot

An interactive AI chatbot built with **Streamlit** and powered by **Groq API** for fast LLM responses.  
The chatbot provides a simple web interface for real-time conversation.

---

## 📌 Features
- 🗨️ **Web-based Chat UI** – Built with Streamlit.
- ⚡ **Groq LLM Integration** – Fast and accurate AI responses.
- 📡 **Real-Time Streaming** – Responses appear as they are generated.
- 🎯 **Customizable** – Easily change the prompt or behavior.
- 📦 **Lightweight** – Minimal dependencies, easy to deploy.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **[Streamlit](https://streamlit.io/)** – Web interface
- **[Groq API](https://groq.com/)** – Large Language Model
- **[Requests / Groq SDK](https://pypi.org/project/groq/)** – API calls

---

## 📂 Project Structure
```
project-folder/
│
├── app.py                # Streamlit chatbot app
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (GROQ_API_KEY)
└── README.md             # Documentation
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables
Create a `.env` file in the project folder and add:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Chatbot
```bash
streamlit run app.py
```
Then open the **local URL** shown in your terminal (usually `http://localhost:8501`).

---

## 💡 Usage
1. Type your question in the input box.
2. The chatbot will stream a real-time response from the Groq LLM.
3. Continue chatting naturally.



## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.
