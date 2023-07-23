from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1

        time_left = seconds - time_elapsed
        
        weeks_left = int(time_left // 604800)
        days_left = int(time_left // 86400) % 7
        hours_left = int(time_left // 3600) % 24
        minutes_left = int(time_left // 60) % 60
        seconds_left = time_left % 60
       
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {weeks_left:02d} WEEKS: {days_left:02d} DAYS: {hours_left:02d} HOURS: {minutes_left:02d} MINUTES: {seconds_left:02d} SECONDS")

    playsound('D:\\GITHUBREPOv2\\Programming-Tasks-Projects\\Python\\Projects\\Alarm Clock Project\\iPhone_Alarm_Original.mp3')

weeks = int(input("How many weeks to wait: "))
days = int(input("How many days to wait: "))
hours = int(input("How many hours to wait: "))
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))

total_seconds = weeks * 604800 + days * 86400 + hours * 3600 + minutes * 60 + seconds
alarm(total_seconds)


