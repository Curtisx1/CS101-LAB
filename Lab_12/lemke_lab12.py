# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 12
# Due Date: 11/16/2022
# Created date: 11/16/2022


# Imported Libraries
import time

# Class


class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int, option: int = 0) -> None:

        if hour >= 60:
            raise ValueError("Must be less than 60.")
        if minutes >= 60:
            raise ValueError("Must be less than 60.")
        if seconds >= 60:
            raise ValueError("Must be less than 60.")




        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.option = option

    def tick(self):
        self.seconds += 1
        self.minutes += self.seconds // 60
        self.hour += self.minutes // 60
        self.seconds = self.seconds % 60
        self.minutes = self.minutes % 60
        self.hour = self.hour % 24

    def __str__(self) -> str:
        hour_print = self.hour
        minute_print = self.minutes
        second_print = self.seconds
        if self.option == 1:
            if hour_print < 12:
                if hour_print == 0:
                    hour_print = 12
                time_return = f"{hour_print:02}:{minute_print:02}:{second_print:02} am"
            else:
                if hour_print > 12:
                    hour_print -= 12
                time_return = f"{hour_print:02}:{minute_print:02}:{second_print:02} pm"

        else:
            time_return = f"{hour_print:02}:{minute_print:02}:{second_print:02}"
        return time_return


    # def errors(self):
    #     while True:
    #         try:
    #             self.hour = int(input("Enter current hour:"))
    #             self.minutes = int(input("Enter current minute:"))
    #             self.seconds = int(input("Enter current second:"))
    #             return self.hour, self.minutes, self.seconds
    #         except ValueError:
    #             print("Value not in range. Please try again.")

# Main program


if __name__ == "__main__":
    hour = int(input("Enter current hour:"))
    minute = int(input("Enter current minute:"))
    second = int(input("Enter current second:"))

    clockObj = Clock(hour, minute, second, option=1)

    while True:
        print(clockObj)
        clockObj.tick()
        time.sleep(1)
