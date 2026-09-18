# 🏥 PhysioVision
### AI Powered Physiotherapy Monitoring System using Computer Vision

PhysioVision is an intelligent physiotherapy assistance system employing Computer Vision, MediaPipe, and OpenCV to provide real-time monitoring of physiotherapy exercises. The system detects body posture, tracks joint angle, counts repetitions, evaluates exercise performance, stores history of patient sessions, and generates performance reports.

PhysioVision aims to assist patients to execute appropriate physiotherapy exercises at home, while also providing relevant analytics to the physiotherapist.
---

## 📌 Problem Statement

Physiotherapy requires patients to perform a series of rehabilitation exercises. However, the rehabilitation exercises are performed without the direct supervision of a physiotherapist, which may cause the patients to perform the exercises incorrectly, thus, reducing the efficacy of the rehabilitation and increasing the chances of sustaining injuries.

PhysioVision solves this problem by providing:

- Real-time pose detection

- Real-time repetition counter

- Automatic exercise evaluation

- Session history

- Analytics dashboard

- PDF report generation
---
## 🎯 Objectives
- Detect and track Human body posture using Computer Vision.
- Calculate angles for executing each exercise.
- Automatic counting of repetitions.

- Evaluate exercise performance.
- Store history of physiotherapy exercise sessions.
- Generate physiotherapy progress reports.
- Provide rehabilitation progress analytics.
---
## ✨ Features

### 👤 Patient Registration
- Register physiotherapy patients.
- Store patient information.
- Track exercise sessions per patient.

### 📷 Real-Time Pose Detection
- Uses MediaPipe Pose Estimation.
- Detects body landmarks from webcam feed.
- Tracks posture during exercises.

### 💪 Multi-Exercise Support

Currently supported exercises:

1. Arm Curl
2. Shoulder Raise
3. Knee Bend

### 📐 Joint Angle Calculation
- Calculates body joint angles.
- Provides movement analysis.
- Supports exercise-specific tracking.

### 🔢 Repetition Counter
- Automatically counts repetitions.
- Detects complete movement cycles.
- Tracks exercise progress.

### 🧠 Exercise Evaluation
- Evaluates exercise correctness.
- Provides real-time feedback.
- Detects improper movement patterns.

### 🗄️ Session Management
- Stores exercise sessions in SQLite.
- Records:
  - Patient Name
  - Exercise Type
  - Repetitions
  - Accuracy
  - Session Date

### 📊 Analytics Dashboard
- Total Sessions
- Total Repetitions
- Average Accuracy
- Exercise Distribution
- Session History
- Accuracy Trends

### 📋 Patient History
- View historical exercise sessions.
- Filter patient records.
- Monitor rehabilitation progress.

### 📄 PDF Report Generation
- Generate patient progress reports.
- Download reports for therapists and patients.

---

## 🏗️ System Architecture
```text
Webcam
│
▼
OpenCV Video Capture
│
▼
MediaPipe Pose Detection
│
▼
Joint Angle Calculation
│
▼
Exercise Evaluation
│
▼
Rep Counter
│
▼
SQLite Database
│
▼
Streamlit Dashboard
│
▼
PDF Report Generation
```
---
## 🛠️ Technology Stack
| Technology | Description |
| --- | --- |
| Programming Language | Python 3.11 |
| Computer Vision | OpenCV, MediaPipe |
| Database | SQLite |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Report Generation | ReportLab |
| Version Control | Git, GitHub |
---
## 📂 Project Structure
```text
PhysioVision/
│
├── app.py
├── requirements.txt
├── README.md
├── statement.md
│
├── database/
│  └── physiovision.db
│
├── reports/
│
├── src/
│  ├── pose_detector.py
│  ├── angle_calculator.py
│  ├── rep_counter.py
│  ├── exercise_manager.py
│  ├── exercise_evaluator.py
│  ├── accuracy_calculator.py
│  ├── database_manager.py
│  └── report_generator.py
│
├── streamlit_app/
│  ├── dashboard.py
│  ├── patient_registration.py
│  └── patient_history.py
│
└── screenshots/
```
---
## ⚙️ Installation
### Clone Repository
```bash

git clone https://github.com/Akansha-upadhyay/PhysioVision.git
cd PhysioVision
```
### Create Virtual Environment
```bash
python3.11 -m venv venv
```
### Activate Environment
Mac/Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
---
## ▶️ Running the Application
### Run Physiotherapy Exercise Tracker
```bash
python app.py
```
Select Exercise:
```text
1. Arm Curl
2. Shoulder Raise
3. Knee Bend
```
Press:
```text
q
```
to stop the session.
---
## 📊 Run Dashboard
```bash
streamlit run streamlit_app/dashboard.py
```
Open:
```text
http://localhost:8501
```
---
## 📋 Run Patient History
```bash
streamlit run streamlit_app/patient_history.py
```
---
## 🧪 Testing
### Test Cases
| Test Case | Expected Result |
|------------|----------------|
| Arm Curl Detection | Correct Rep Count |
| Shoulder Raise Detection | Correct Rep Count |
| Knee Bend Detection | Correct Rep Count |
| Database Save | Session Stored |
| Dashboard Analytics | Data Displayed |
| PDF Generation | Report Downloaded |
---
## 📈 Results
The system successfully:
- Detects physiotherapy exercises
- Calculates body angles
- Counts repetitions automatically
- Evaluates exercise performance
- Stores patient history
- Generates PDF reports
- Provides rehabilitation analytics
---
## 🔒 Non-Functional Requirements
| Non-Functional Requirement | Description |
|--- | --- |
| Performance | Real-time pose detection and angle calculation. |
| Reliability | Stable exercise tracking and session storage. |
| Usability | Simple user interface for patients and therapists. |
| Maintainability | Modular architecture for future enhancements. |
| Scalability | Can support additional exercises and users. |
| Security | Local database storage for patient records. |
---
## 🚀 Future Enhancements
- AI-Based Posture Correction
- Voice Feedback Assistant
- Therapist Portal
- Cloud Database Integration
- Mobile Application
- Exercise Recommendation System
- Tele-Rehabilitation Support
- Deep Learning-Based Movement Assessment
---
## 👩‍💻 Author
Akansha Upadhyay

B.Tech CSE (AI & ML)

VIT Bhopal University
---

## 📜 License

This project is developed for academic and educational purposes as a part of the Computer Vision course project at VIT Bhopal University.
