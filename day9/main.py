import time #import time module
def countdown_timer(seconds):
    while seconds:
        hrs,min,sec=seconds//3600,(seconds%3600)//60,seconds%60
        timer_format=f'{hrs:02d}:{min:02d}:{sec:02d}'
        print(timer_format,end='\r')
        time.sleep(1)
        seconds-=1
    print("Time's up!")

#User input
try:
    total_seconds=int(input("Enter the time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number.")
