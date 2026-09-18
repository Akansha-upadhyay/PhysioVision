class ExerciseManager:

    EXERCISES = {

        "Arm Curl": {
            "points": (
                "LEFT_SHOULDER",
                "LEFT_ELBOW",
                "LEFT_WRIST"
            ),
            "up_angle": 60,
            "down_angle": 150,
            "description": "Bicep Curl Exercise",
            "feedback_good": "Good Curl"
        },

        "Shoulder Raise": {
            "points": (
                "LEFT_HIP",
                "LEFT_SHOULDER",
                "LEFT_ELBOW"
            ),
            "up_angle": 80,
            "down_angle": 20,
            "description": "Shoulder Rehabilitation Exercise",
            "feedback_good": "Good Raise"
        },

        "Knee Bend": {
            "points": (
                "LEFT_HIP",
                "LEFT_KNEE",
                "LEFT_ANKLE"
            ),
            "up_angle": 100,
            "down_angle": 170,
            "description": "Knee Physiotherapy Exercise",
            "feedback_good": "Good Bend"
        }
    }

    @staticmethod
    def get_exercise(name):
        return ExerciseManager.EXERCISES.get(name)

    @staticmethod
    def get_all_exercises():
        return list(
            ExerciseManager.EXERCISES.keys()
        )

    @staticmethod
    def print_exercises():

        print("\nAvailable Exercises\n")

        for index, exercise in enumerate(
            ExerciseManager.get_all_exercises(),
            start=1
        ):
            print(f"{index}. {exercise}")

    @staticmethod
    def get_exercise_by_choice(choice):

        mapping = {
            "1": "Arm Curl",
            "2": "Shoulder Raise",
            "3": "Knee Bend"
        }

        return mapping.get(
            choice,
            "Arm Curl"
        )