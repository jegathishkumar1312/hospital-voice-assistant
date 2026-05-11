import streamlit as st
from streamlit_mic_recorder import speech_to_text
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

# ---------------- VOICE INPUT ---------------- #

st.subheader("Voice Input")

voice_text = speech_to_text(
    language="en",
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    use_container_width=True,
    just_once=True,
    key="voice_input"
)

# ---------------- TEXT INPUT ---------------- #

user_input = st.text_input(
    "Enter your hospital question",
    value=voice_text if voice_text else ""
)

# ---------------- ASK BUTTON ---------------- #

if st.button("Ask"):

    query = user_input.lower().strip()

    intent = "unknown"

    # ---------------- IMPROVED NLP MATCHING ---------------- #

    if "icu" in query or "i see you" in query:
        intent = "icu"

    elif "pharmacy" in query:
        intent = "pharmacy"

    elif "emergency" in query:
        intent = "emergency"

    elif "op" in query:
        intent = "op"

    elif "cardiology" in query:
        intent = "cardiology"

    elif "radiology" in query:
        intent = "radiology"

    elif "lab" in query or "laboratory" in query:
        intent = "lab"

    # ---------------- RESPONSE ---------------- #

    answer = hospital_data.get(
        intent,
        "Sorry, information not available"
    )

    # ---------------- SAVE TRANSCRIPT ---------------- #

    save_transcript(query, intent, answer)

    # ---------------- DISPLAY OUTPUT ---------------- #

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
