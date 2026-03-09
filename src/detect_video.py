from ultralytics import YOLO
import cv2
import time
import threading
try:
    import winsound
except:
    winsound = None
import requests
import json

# ===============================
# TELEGRAM SETTINGS
# ===============================

BOT_TOKEN = "8174249575:AAFuE_qwKqy9kaMyQ5BNcDrvu7sMaE6bfpI"

def load_users():
    try:
        with open("users.json","r") as f:
            return json.load(f)
    except:
        return []

def send_telegram_alert():

    users = load_users()

    for chat_id in users:

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": "🔥 FIRE DETECTED! Check camera immediately."
            }
        )


def send_fire_image(image_path):

    users = load_users()

    for chat_id in users:

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

        files = {"photo": open(image_path,"rb")}

        requests.post(url,data={"chat_id":chat_id},files=files)


def send_fire_video(video_path):

    users = load_users()

    for chat_id in users:

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"

        files = {"video": open(video_path,"rb")}

        requests.post(url,data={"chat_id":chat_id},files=files)


# ===============================
# ALARM SOUND
# ===============================

def play_alarm():
    if winsound:
        winsound.Beep(2000,500)


# ===============================
# LOAD MODEL
# ===============================

model = YOLO("models/fire_model.pt")


# ===============================
# ALERT CONTROL
# ===============================

last_alert_time = 0
alert_interval = 10


# ===============================
# VIDEO RECORDING SETTINGS
# ===============================

recording = False
video_writer = None
record_start = None
record_duration = 10
video_name = None


# ===============================
# DETECTION FUNCTION
# ===============================

def detect_frame(frame):

    global last_alert_time
    global recording
    global video_writer
    global record_start
    global video_name

    results = model(frame, conf=0.5)

    annotated_frame = results[0].plot()

    fire_detected = False
    fire_conf = 0

    for box in results[0].boxes:

        cls = int(box.cls)
        conf = float(box.conf)

        if cls == 0 and conf > 0.80:

            fire_detected = True
            fire_conf = conf


    if fire_detected:

        cv2.putText(
            annotated_frame,
            f"🔥 FIRE {round(fire_conf*100,1)}%",
            (40,60),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0,0,255),
            3
        )

        threading.Thread(target=play_alarm).start()

        current_time = time.time()

        # SEND TELEGRAM ALERT + SCREENSHOT
        if current_time - last_alert_time > alert_interval:

            image_name = f"fire_{int(current_time)}.jpg"

            cv2.imwrite(image_name, annotated_frame)

            send_telegram_alert()
            send_fire_image(image_name)

            last_alert_time = current_time


        # START VIDEO RECORDING
    if fire_detected and not recording:

     fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video_name = f"fire_video_{int(current_time)}.mp4"

    video_writer = cv2.VideoWriter(
        video_name,
        fourcc,
        20.0,
        (frame.shape[1], frame.shape[0])
    )

    recording = True
    record_start = time.time()

# SAVE VIDEO FRAME
    if recording and video_writer is not None and record_start is not None:

         video_writer.write(annotated_frame)

         if time.time() - record_start > record_duration:

          recording = False

         video_writer.release()

    if video_name:
            send_fire_video(video_name)

    return annotated_frame