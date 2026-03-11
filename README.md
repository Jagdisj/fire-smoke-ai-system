# 🔥 AI Fire & Smoke Detection System

An AI-powered **Fire and Smoke Detection System** built with **YOLOv8, Python, OpenCV, Streamlit, and the Telegram Bot API**.

The platform detects fire/smoke from **images, videos, and live camera feeds**, then sends **instant Telegram alerts** with screenshot and video evidence for rapid incident response.

---

## 📌 Project Overview

This project is designed as a practical AI safety monitoring solution for real-world surveillance scenarios. It combines deep-learning-based object detection with a lightweight monitoring dashboard and automated alerting pipeline.

### 🧠 System Architecture

```text
Camera / Image / Video
        │
        ▼
YOLOv8 Fire Detection Model
        │
        ▼
Detection Engine (OpenCV)
        │
        ├── Screenshot Capture
        ├── Video Recording
        └── Telegram Alert System
        │
        ▼
Streamlit Monitoring Dashboard
```

---

## ✨ Key Features

- 🔥 Fire & smoke detection using YOLOv8
- 🎥 Video detection support
- 📷 Live CCTV / webcam monitoring
- 📸 Automatic screenshot evidence capture
- 🎬 Automatic video recording on fire detection
- 📲 Telegram alert notifications
- 🌐 Interactive Streamlit monitoring dashboard
- ⚡ Optimized frame processing for faster detection

---

## 🛠 Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- Telegram Bot API

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Jagdishj/fire-smoke-ai-system.git
cd fire-smoke-ai-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Streamlit application

```bash
streamlit run app/dashboard.py
```

Then open:

```text
http://localhost:8501
```

### 🔍 Detection Modes

- **Image Detection**: Upload image and detect fire.
- **Video Detection**: Upload video and run frame-by-frame detection.
- **Live Webcam / CCTV**: Real-time monitoring using webcam or camera feed.

### 🤖 Telegram Alert Setup

#### Step 1 — Create Telegram Bot

1. Open **BotFather** in Telegram.
2. Run command:
   ```text
   /newbot
   ```
3. Copy your **BOT TOKEN**.

#### Step 2 — Add token in code

Update the file:

```text
src/detect_video.py
```

Replace:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
```

#### Step 3 — Start the bot

Open your bot and send:

```text
/start
```

Your chat ID will be automatically registered.

### 📲 Telegram Alert Example

When fire is detected, the system automatically sends:

- ⚠️ Fire detected alert
- 📸 Screenshot evidence
- 🎬 Recorded video clip

Example message:

```text
🔥 FIRE DETECTED!
Check camera immediately.
```

### ⚡ Performance Optimization

To improve speed, the system uses:

- Frame resizing
- Frame skipping
- Efficient YOLO inference

This enables smoother detection even on CPU-only systems.

---

## 📂 Project Structure

```text
fire-smoke-ai-system
│
├── app
│   └── dashboard.py
│
├── src
│   ├── detect_video.py
│   ├── detect.py
│   ├── alert.py
│   ├── telegram_alert.py
│   └── bot_listener.py
│
├── models
│   └── fire_model.pt
│
├── dataset
├── test_images
├── test_videos
│
├── users.json
├── requirements.txt
└── README.md
```

---

## 🚀 Live Demo

### Dashboard Preview

<img width="1915" height="895" alt="Screenshot 2026-03-10 155333" src="https://github.com/user-attachments/assets/699a34ba-63fd-4673-8469-53a5c5820571" />

<img width="1177" height="1009" alt="Screenshot 2026-03-10 153443" src="https://github.com/user-attachments/assets/9403601d-6ed2-470d-89ef-7505ad3287e5" />

<img width="1918" height="896" alt="Screenshot 2026-03-10 154909" src="https://github.com/user-attachments/assets/26c7388c-971b-4e85-8d77-1e5312445f20" />

### Fire Detection Example

<img width="994" height="564" alt="Screenshot 2026-03-10 154230" src="https://github.com/user-attachments/assets/97b2d8ab-cd3c-425e-8b41-300322daed6a" />

### Demo Video

https://github.com/user-attachments/assets/197f4c9e-a32d-40bb-8588-d004369836a7

### Try the Streamlit App Online

🌐 **Streamlit App:** https://fire-smoke-ai-system-dishika0707.streamlit.app/

---

## 🌐 Deployment

This project can be deployed using:

- Streamlit Cloud
- Local server
- VPS / cloud instance

To share a public demo link:

```bash
ngrok http 8501
```

---

## 📌 Future Improvements

- Multi-camera monitoring
- RTSP CCTV support
- Incident history database
- Email alert integration
- Advanced analytics dashboard

---

## 👨‍💻 Author

**E Jagadish**  
AI / Data Scientist Enthusiast

- GitHub: https://github.com/Jagdisj

---

## ⭐ Support

If you found this project useful, please consider supporting it:

- ⭐ Star the repository
- 🍴 Fork the project
