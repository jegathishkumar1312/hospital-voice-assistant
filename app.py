import streamlit as st
import json
import speech_recognition as sr
from datetime import datetime

# Load hospital data
with open("hospital_data.json", "r") as file:
    hospital_data = json.load(file)

# Load transcripts
try:
    with open("transcripts.json", "r") as file:
        transcripts = json.load(file)
except:
    transcripts = []

# Page settings
st.set_page_config(page_title="Hospital Voice Helpdesk")

# Title
st.title("Hospital Voice Helpdesk")

# Description
st.write("Voice-enabled hospital helpdesk system")

st.divider()

# Session state for voice input
if "question" not in st.session_state:
    st.session_state.question = ""

# Text input
question = st.text_input(
    "Enter your hospital question",
    value=st.session_state.question
)

# Voice input button
if st.button("Use Voice Input"):

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            st.info("Listening... Speak now")

            audio = recognizer.listen(source)

            voice_text = recognizer.recognize_google(audio)

            # Save voice text
            st.session_state.question = voice_text

            st.success(f"You said: {voice_text}")

    except:
        st.error("Microphone or voice recognition error")

# Ask button
if st.button("Ask"):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    answer = "Sorry, information not available"

    # Use typed question first
    question = question.lower().strip()

    # If text box empty, use voice input
    if question == "":
        question = st.session_state.question.lower().strip()

    # Search hospital data
    for key in hospital_data:

        if key.lower() in question:

            answer = hospital_data[key]
            break

    # Display answer
    st.success(answer)

    # Display timestamp
    st.info(f"Time: {current_time}")

    # Save transcript
    chat = {
        "question": question,
        "answer": answer,
        "time": current_time
    }

    transcripts.append(chat)

    with open("transcripts.json", "w") as file:
        json.dump(transcripts, file, indent=4)

st.divider()

# Show transcripts
st.subheader("Previous Transcripts")

for chat in transcripts:

    st.write(f"Question: {chat['question']}")
    st.write(f"Answer: {chat['answer']}")
    st.write(f"Time: {chat['time']}")
    st.write("-----------------------------")