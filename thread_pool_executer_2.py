import concurrent.futures
import time

class xyz:

    def __init__(self,start):
        self.start=start
        self.exe()

    def msg(self, sec):
        print(f"sleeping {sec} seconds")
        time.sleep(sec)
        return f"sleeping for {sec}"

    def exe(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # To execute single thread
            # f1=executor.submit(self.msg,5)
            # print(f1.result())

            """to use multiple threads
                This will return us the result in order way no in the way the threads are started"""
            # secs=[5,4,3,2,1]#list of seconds to sleep
            # results=[executor.submit(self.msg,sec) for sec in secs]
            #
            # for f in concurrent.futures.as_completed(results):#To print the result
            #     print(f.result())

            """Alternative way to with using MAP function
                This will give us the results but in order way in which threads are started !"""
            secs = [5, 4, 3, 2, 1]
            results=executor.map(self.msg,secs)

            for f in results:
                print(f)





    def __str__(self):
        return f"Program Finished in {round(time.perf_counter()-self.start)} seconds"

if __name__=="__main__":
    x=xyz(time.perf_counter())
    print(x)





