# 🏥 PhysioVision
### AI-Powered Physiotherapy Monitoring System using Computer Vision

PhysioVision is an intelligent physiotherapy assistance system that uses **Computer Vision**, **MediaPipe**, and **OpenCV** to monitor rehabilitation exercises in real time. The system tracks body posture, calculates joint angles, counts exercise repetitions, evaluates exercise quality, stores patient session history, and generates performance reports.

This project aims to help patients perform physiotherapy exercises correctly at home while providing therapists with objective progress tracking and analytics.

---

## 📌 Problem Statement

Patients undergoing physiotherapy often perform rehabilitation exercises without continuous supervision. Incorrect posture, improper movement, and inaccurate repetitions can reduce recovery effectiveness and increase the risk of injury.

PhysioVision addresses this challenge by providing:

- Real-time pose detection
- Automatic repetition counting
- Exercise quality evaluation
- Session history tracking
- Performance analytics dashboard
- PDF report generation

---

## 🎯 Objectives

- Detect and track human body posture using Computer Vision.
- Calculate exercise angles in real time.
- Count repetitions automatically.
- Evaluate exercise performance.
- Store patient exercise sessions.
- Generate physiotherapy progress reports.
- Visualize rehabilitation progress through dashboards.

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

### Programming Language
- Python 3.11

### Computer Vision
- OpenCV
- MediaPipe

### Database
- SQLite

### Dashboard
- Streamlit

### Data Processing
- Pandas
- NumPy

### Report Generation
- ReportLab

### Version Control
- Git
- GitHub

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
│   └── physiovision.db
│
├── reports/
│
├── src/
│   ├── pose_detector.py
│   ├── angle_calculator.py
│   ├── rep_counter.py
│   ├── exercise_manager.py
│   ├── exercise_evaluator.py
│   ├── accuracy_calculator.py
│   ├── database_manager.py
│   └── report_generator.py
│
├── streamlit_app/
│   ├── dashboard.py
│   ├── patient_registration.py
│   └── patient_history.py
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

- Detects physiotherapy exercises.
- Calculates body angles.
- Counts repetitions automatically.
- Evaluates exercise quality.
- Stores patient history.
- Generates PDF reports.
- Provides rehabilitation analytics.

---

## 🔒 Non-Functional Requirements

### Performance
Real-time pose detection and angle calculation.

### Reliability
Stable exercise tracking and session storage.

### Usability
Simple user interface for patients and therapists.

### Maintainability
Modular architecture for future enhancements.

### Scalability
Can support additional exercises and users.

### Security
Local database storage for patient records.

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

## 📚 References

- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
- :contentReference[oaicite:3]{index=3}

---

## 👩‍💻 Author

**Akansha Upadhyay**

B.Tech CSE (AI & ML)

VIT Bhopal University

---

## 📜 License

This project is developed for academic and educational purposes as part of the Computer Vision course project at VIT Bhopal University.
