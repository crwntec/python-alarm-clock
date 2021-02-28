#Import Packages
from playsound import playsound
import datetime
from datetime import datetime
import time

#Get Alarm Time from User Input
alarm_time = input('Enter the alarm-time in the format HH:MM \n')

#Split and convert it into Integerformat
hour, minute = map(int, alarm_time.split(':'))

class alarm:
    def start(self, hour, minute, run):
        run = True
        while run:
            time.sleep(1)   #Wait one sec.
            a = datetime.now() #Get current time
            if a.hour == hour and a.minute == minute:   #compare current time with alarm time
                print("ALARM!")
                playsound("alarm.mp3")  #play alarm sound
                run = False #quit loop

n_alarm = alarm()   #create instance
n_alarm.start(hour, minute, True)   #start alarm