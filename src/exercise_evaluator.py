class ExerciseEvaluator:

    def evaluate(self, exercise, angle):

        if exercise == "Arm Curl":

            if angle < 60:
                return "Good Curl"

            elif angle < 120:
                return "Keep Going"

            else:
                return "Lower Arm"

        elif exercise == "Shoulder Raise":

            if angle > 80:
                return "Good Raise"

            else:
                return "Raise Higher"

        elif exercise == "Knee Bend":

            if angle < 100:
                return "Good Bend"

            else:
                return "Bend More"

        return "Tracking"