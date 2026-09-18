class RepCounter:

    def __init__(self):

        self.counter = 0
        self.stage = "down"

    def update(
        self,
        angle,
        up_angle,
        down_angle
    ):

        if angle > down_angle:
            self.stage = "down"

        if angle < up_angle and self.stage == "down":

            self.stage = "up"
            self.counter += 1

        return self.counter