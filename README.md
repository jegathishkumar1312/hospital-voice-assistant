# 🏥 Hospital Voice Helpdesk

## 🌐 Live Application

🔗 Streamlit Cloud Deployment:

[https://mvdzhwlpvjeiazckeadpkp.streamlit.app/](https://mvdzhwlpvjeiazckeadpkp.streamlit.app/)

Voice + NLP powered hospital assistant built using FastAPI and Streamlit.

---

# 📌 Project Overview

Hospital Voice Helpdesk is a kiosk-style AI assistant designed to help patients and visitors inside hospitals using voice and text interaction.

The system provides:

* Department directions
* Hospital information
* Voice-based interaction
* NLP intent detection
* Transcript storage and replay
* Real-time response generation

This project was developed as a GenAI + NLP mini project.

---

# 🚀 Features

| Feature                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| 🎤 Voice Input          | Accepts voice queries using browser microphone |
| 📝 Speech-to-Text       | Converts spoken audio into text                |
| 🧠 NLP Intent Detection | Detects hospital-related intents               |
| 💬 Response Generation  | Generates department/location responses        |
| 📂 Transcript Storage   | Stores user conversations in JSON              |
| 🔁 Transcript Replay    | Displays previous conversation history         |
| 🌐 Streamlit UI         | Interactive frontend interface                 |
| ⚡ FastAPI Backend       | Backend API handling                           |

---

# 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Streamlit  | Frontend user interface   |
| FastAPI    | Backend API framework     |
| NLP        | Intent detection          |
| JSON       | Transcript storage        |
| GitHub     | Version control           |

---

# 🏗️ System Architecture

```text
+-------------------+
|   User Voice/Text |
+-------------------+
          |
          v
+-------------------+
| Speech-to-Text    |
| (Voice Processing)|
+-------------------+
          |
          v
+-------------------+
| NLP Intent Engine |
+-------------------+
          |
          v
+-------------------+
| Domain Database   |
+-------------------+
          |
          v
+-------------------+
| Response Generator|
+-------------------+
          |
          v
+-------------------+
| Streamlit UI      |
+-------------------+
          |
          v
+-------------------+
| Transcript Store  |
+-------------------+
```

---

# 📂 Project Structure

```text
hospital-voice-helpdesk/
│
├── app.py
├── main.py
├── transcripts.json
├── requirements.txt
├── README.md
└── nlp_engine.py
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/hospital-voice-helpdesk.git
```

---

## 2️⃣ Open Project Folder

```bash
cd hospital-voice-helpdesk
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start FastAPI Backend

```bash
py -m uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🧠 NLP Workflow

```text
User Query
     |
     v
Text Preprocessing
     |
     v
Intent Detection
     |
     v
Hospital Data Matching
     |
     v
Response Generation
```

---

# 📊 Sample Queries

| User Query        | Detected Intent | Response                    |
| ----------------- | --------------- | --------------------------- |
| Where is ICU?     | icu             | ICU is located on 2nd floor |
| Pharmacy location | pharmacy        | Pharmacy near reception     |
| Emergency ward    | emergency       | Emergency ward open 24/7    |
| OP department     | op              | OP on ground floor          |

---

# 🧪 Testing

## Week 1 Testing

| Test Case            | Result   |
| -------------------- | -------- |
| Text input handling  | ✅ Passed |
| API response testing | ✅ Passed |
| Sample inference     | ✅ Passed |
| Preprocessing        | ✅ Passed |

---

## Week 2 Testing

| Test Case        | Result   |
| ---------------- | -------- |
| Intent detection | ✅ Passed |
| Voice input      | ✅ Passed |
| Boundary cases   | ✅ Passed |
| Response latency | ✅ Passed |

---

# 📸 Demo Workflow

1. User opens Streamlit application
2. User enters voice or text query
3. NLP engine detects intent
4. System generates hospital response
5. Transcript stored in JSON
6. Previous conversations displayed

---

# 🔮 Future Enhancements

* Multilingual support
* Real hospital database integration
* AI chatbot enhancement
* Appointment booking
* Text-to-speech responses
* Cloud database integration

---

# 📈 Project Outcome

The Hospital Voice Helpdesk successfully demonstrates:

* NLP-based hospital assistance
* Voice-enabled interaction
* Real-time response generation
* API integration
* Transcript management
* User-friendly interface

---

# 👨‍💻 Developed By

Jegathish Kumar

ECE Student

---

# 📜 License

This project is developed for educational and academic purposes.
