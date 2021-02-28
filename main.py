from playsound import playsound
import datetime
from datetime import datetime
import time
alarm_time = input('Enter the alarm-time in the format HH:MM \n')

hour, minute = map(int, alarm_time.split(':'))

class alarm:
    def start(self, hour, minute, run):
        run = True
        while run:
            time.sleep(1)
            a = datetime.now()
            if a.hour == hour and a.minute == minute:
                print("ALARM!")
                playsound("alarm.mp3")
                run = False

n_alarm = alarm()
n_alarm.start(hour, minute, True)