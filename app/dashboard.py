import streamlit as st
import cv2
import tempfile
import sys
import os
import json
import requests

BOT_TOKEN = "8174249575:AAFuE_qwKqy9kaMyQ5BNcDrvu7sMaE6bfpI"

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from detect_video import detect_frame

st.set_page_config(
    page_title="AI Fire Monitoring",
    layout="wide",
    page_icon="🔥"
)

# ============================
# LOAD USERS
# ============================

def get_users():

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

    data = requests.get(url).json()

    users = []

    for result in data.get("result", []):

        message = result.get("message")

        if message:

            chat_id = message["chat"]["id"]

            if chat_id not in users:
                users.append(chat_id)

    return users


users = get_users()

# ============================
# LOGIN CHECK
# ============================

if len(users) == 0:

    st.title("🔥 Login Required")

    st.write("Open Telegram bot and send /start")

    st.markdown("👉 https://t.me/fire_alert_admin_ai_bot")

    st.stop()


# ============================
# DASHBOARD
# ============================

st.title("🔥 AI Fire Monitoring Dashboard")
st.write("Fire & Smoke Detection System")


option = st.selectbox(
    "Select Detection Source",
    ("Image Detection", "Video Detection", "Live CCTV / Webcam")
)

# ============================
# IMAGE DETECTION
# ============================

if option == "Image Detection":

    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if uploaded_file:

        file_bytes = uploaded_file.read()

        with open("temp.jpg","wb") as f:
            f.write(file_bytes)

        image = cv2.imread("temp.jpg")

        annotated = detect_frame(image)

        st.image(annotated, channels="BGR")


# ============================
# VIDEO DETECTION
# ============================

elif option == "Video Detection":

    uploaded_video = st.file_uploader("Upload Video", type=["mp4","avi","mov"])

    if uploaded_video:

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)

        frame_window = st.image([])

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            annotated = detect_frame(frame)

            frame_window.image(annotated, channels="BGR")

        cap.release()


# ============================
# LIVE CCTV / WEBCAM
# ============================

elif option == "Live CCTV / Webcam":

    start = st.button("Start Camera")

    if start:

        cap = cv2.VideoCapture(0)

        frame_window = st.image([])

        while True:

            ret, frame = cap.read()

            if not ret:
                st.error("Camera error")
                break

            annotated = detect_frame(frame)

            frame_window.image(annotated, channels="BGR")

        cap.release()