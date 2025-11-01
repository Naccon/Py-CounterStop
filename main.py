import time
from art import art
print(art)
txt="Welcome to Py-CounterStop"
for char in txt:
    print(char,end="",flush=True)
    time.sleep(0.2)
print()
start=True
my_time=0
def user_time():
    time_opt=int(input("Enter time in\n[1]\tSecond\n[2]\tMinute\n[3]\tHour\n"))
    if time_opt==1:
        my_time=int(input("Please enter the total number of seconds: "))
    elif time_opt==2:
        my_time=int(input("Please enter the total number of minutes: "))*60
    elif time_opt==3:
        my_time=int(float(input("Please enter the total number of hours: "))*3600)
    else:
        print("Oops! Invalid choice. Setting default time to 1 hour.")
        my_time=3600
    return my_time
while start:
    user_choice = int(input("Please choose an option:\n[1]\tStart Count\n[2]\tStart Stopwatch\n[0]\tExit Program\n"))
    if user_choice==1:
        my_time=user_time()
        for x in range(0,my_time+1,1):
            second=x%60
            minute=int(x/60)%60
            hour=int(x/3600)
            print(f"{hour:02}:{minute:02}:{second:02}")
            time.sleep(1)
    elif user_choice==2:
        my_time=user_time()
        for x in range(my_time,-1,-1):
            second = x % 60
            minute = int(x / 60) % 60
            hour = int(x / 3600)
            print(f"{hour:02}:{minute:02}:{second:02}")
            time.sleep(1)
    elif user_choice==0:
        print("Stopping program ", end="", flush=True)
        for _ in range(4):
            time.sleep(1)
            print(".", end="", flush=True)
        break
    else:
        print("Invalid choice")
