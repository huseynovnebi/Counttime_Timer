import time

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds 
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')  
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        countdown_timer(minutes, seconds)
    except ValueError:
        print("Please enter valid numbers!")
