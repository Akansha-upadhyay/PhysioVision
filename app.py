import cv2
import mediapipe as mp

from src.pose_detector import PoseDetector
from src.angle_calculator import calculate_angle
from src.rep_counter import RepCounter
from src.exercise_evaluator import ExerciseEvaluator
from src.exercise_manager import ExerciseManager
from src.database_manager import DatabaseManager


# Database
db = DatabaseManager()

# Patient Information
patient_name = input("Enter Patient Name: ")

ExerciseManager.print_exercises()

choice = input(
    "\nEnter choice: "
)

exercise = ExerciseManager.get_exercise_by_choice(
    choice
)

# Load Exercise Configuration
config = ExerciseManager.get_exercise(exercise)

# Initialize Components
cap = cv2.VideoCapture(0)

pose_detector = PoseDetector()
counter = RepCounter()
evaluator = ExerciseEvaluator()

correct_reps = 0

mp_pose = mp.solutions.pose

print(f"\nStarting {exercise} Tracking...")
print("Press Q to Quit\n")

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    results = pose_detector.detect_pose(frame)

    try:

        landmarks = results.pose_landmarks.landmark

        p1 = getattr(
            mp_pose.PoseLandmark,
            config["points"][0]
        )

        p2 = getattr(
            mp_pose.PoseLandmark,
            config["points"][1]
        )

        p3 = getattr(
            mp_pose.PoseLandmark,
            config["points"][2]
        )

        point1 = [
            landmarks[p1.value].x,
            landmarks[p1.value].y
        ]

        point2 = [
            landmarks[p2.value].x,
            landmarks[p2.value].y
        ]

        point3 = [
            landmarks[p3.value].x,
            landmarks[p3.value].y
        ]

        angle = calculate_angle(
            point1,
            point2,
            point3
        )

        reps = counter.update(
            angle,
            config["up_angle"],
            config["down_angle"]
        )

        feedback = evaluator.evaluate(
            exercise,
            angle
        )

        if feedback in [
            "Good Curl",
            "Good Raise",
            "Good Bend"
        ]:
            correct_reps += 1

        # Display Information

        cv2.putText(
            frame,
            f"Patient: {patient_name}",
            (20, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Exercise: {exercise}",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Angle: {int(angle)}",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Reps: {reps}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            feedback,
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    except Exception:
        pass

    frame = pose_detector.draw_landmarks(
        frame,
        results
    )

    cv2.imshow(
        "PhysioVision",
        frame
    )

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


# Calculate Accuracy

if counter.counter > 0:

    accuracy = round(
        (correct_reps / counter.counter) * 100,
        2
    )

else:

    accuracy = 0


# Save Session

db.save_session(
    patient_name,
    exercise,
    counter.counter,
    accuracy
)

print("\n==============================")
print("SESSION SAVED")
print("==============================")
print(f"Patient  : {patient_name}")
print(f"Exercise : {exercise}")
print(f"Reps     : {counter.counter}")
print(f"Accuracy : {accuracy}%")
print("==============================\n")

cap.release()
cv2.destroyAllWindows()