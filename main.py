import time
import threading

start=time.perf_counter()

def msg():
    print("hello")
    time.sleep(2)
    print("sleep for 2 sec !")

def msg2():
    print("second func")
    time.sleep(2)
    print("second sleep for 2 sec !")
# empty list just to store the threads

lst_thread=[]
for _ in range(10):
    t=threading.Thread(target=msg)
    t.start() #starting the thread here and then just appending them to a list
    lst_thread.append(t)

"""In order to use multiple threads at one time we have to store them in one list and then we have to join that list!"""
for thread in lst_thread:
    thread.join()
finish=time.perf_counter()
print(f"Finished in {round(finish-start,2)} seconds")