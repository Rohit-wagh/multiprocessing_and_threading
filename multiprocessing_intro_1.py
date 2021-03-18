import multiprocessing
import time

class xy:
    def __init__(self,start):
        self.start=start
        self.iter_process()

    def mlt_process(self):
        p1=multiprocessing.Process(target=self.msg)
        p2=multiprocessing.Process(target=self.msg)

        p1.start()
        p2.start()

        p1.join()
        p2.join()

    """Another way to run multiple process at same time is using the for loop"""
    def iter_process(self):
        lst_process=[]
        for _ in range(10):
            p=multiprocessing.Process(target=self.msg,args=[10])
            p.start()
            lst_process.append(p)

        for f in lst_process:
            f.join()



    def msg(self,sec):
        print("\nI'm Inside the function")
        time.sleep(sec)
        print(f"\nDone Sleeping for {sec} secs ")

    def __str__(self):
        return f"Program finished in {round(time.perf_counter()-self.start,2)} seconds"

if __name__=="__main__":
    x=xy(time.perf_counter())
    print(x)