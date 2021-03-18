import time
import threading

class thrd:
    start=time.perf_counter()

    def __init__(self,n,start):
        self.n=n
        self.start=start
        thread_lst=[]

        for _ in range(self.n):
            t=threading.Thread(target=self.msg,args=[1.5])
            t.start()
            thread_lst.append(t)

        for thread in thread_lst:
            thread.join()

    def __str__(self):
        return f"Finshed in {round(time.perf_counter()-self.start,2)}"

    def msg(self,seconds):
        print("Inside msg Function !")
        time.sleep(seconds)

if __name__=="__main__":
    x=thrd(10,time.perf_counter())
    print(x)