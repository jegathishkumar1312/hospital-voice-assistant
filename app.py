import streamlit as st
import speech_recognition as sr
import json
import os
from datetime import datetime

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(page_title="Hospital Voice Helpdesk")

st.title("Hospital Voice Helpdesk (NLP System)")
st.write("Voice + NLP powered hospital assistant")

# ---------------- DOMAIN DATABASE ---------------- #

hospital_data = {
    "icu": "ICU is located on 2nd floor, Block A",
    "pharmacy": "Pharmacy is near reception",
    "op": "OP department is on ground floor",
    "emergency": "Emergency ward is open 24/7",
    "cardiology": "Cardiology department is in Block B",
    "radiology": "Radiology department is in Block C",
    "lab": "Laboratory is on 1st floor"
}

# ---------------- TRANSCRIPT STORAGE ---------------- #

def save_transcript(query, intent, answer):

    data = {
        "query": query,
        "intent": intent,
        "answer": answer,
        "time": str(datetime.now())
    }

    if os.path.exists("transcripts.json"):

        try:
            with open("transcripts.json", "r") as f:
                chats = json.load(f)

        except:
            chats = []

    else:
        chats = []

    chats.append(data)

    with open("transcripts.json", "w") as f:
        json.dump(chats, f, indent=4)

# ---------------- VOICE RECOGNITION ---------------- #

def recognize_voice():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        st.info("Speak now...")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text.lower()

        except:
            return ""

# ---------------- SESSION STATE ---------------- #

if "user_query" not in st.session_state:
    st.session_state.user_query = ""

# ---------------- TEXT INPUT ---------------- #

user_input = st.text_input(
    "Enter your hospital question",
    value=st.session_state.user_query
)

# ---------------- VOICE BUTTON ---------------- #

if st.button("Voice Input"):

    voice_text = recognize_voice()

    if voice_text != "":

        st.session_state.user_query = voice_text

        st.success(f"You said: {voice_text}")

        st.rerun()

    else:
        st.error("Could not recognize voice")

# ---------------- ASK BUTTON ---------------- #

if st.button("Ask"):

    query = user_input.lower().strip()

    intent = "unknown"

    # NLP Intent Detection
    for key in hospital_data:

        if key.lower() in query:
            intent = key
            break

    # Response Generation
    answer = hospital_data.get(
        intent,
        "Sorry, information not available"
    )

    # Save Transcript
    save_transcript(query, intent, answer)

    # Display Output
    st.success(answer)

    st.write(f"Intent: {intent}")
    st.write(f"Time: {datetime.now()}")

# ---------------- TRANSCRIPT REPLAY ---------------- #

st.subheader("Previous Transcripts")

if os.path.exists("transcripts.json"):

    try:

        with open("transcripts.json", "r") as f:
            chats = json.load(f)

        for chat in reversed(chats):

            st.write(f"Q: {chat['query']}")
            st.write(f"Intent: {chat['intent']}")
            st.write(f"A: {chat['answer']}")
            st.write(f"Time: {chat['time']}")
            st.write("---")

    except:
        st.error("Transcript file is corrupted")