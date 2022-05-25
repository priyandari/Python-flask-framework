from time import *
import threading


# tIMER
def countdown():
    global my_timer
    my_timer = 10
    for x in range(10):
        my_timer = my_timer-1
        sleep(1)
    print("out of time")

countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()

while my_timer > 0:
    print("hello world 1")
    data = input("input data : ")
    sleep(2)
    if my_timer == 0:
        break
    
    print("hello world 2")
    data = input("input data : ")
    sleep(2)
    if my_timer == 0:
        break

    print("hello world 3")
    data = input("input data : ")
    sleep(2)
    if my_timer == 0:
        break