import time
import concurrent.futures

class eg:
    def __init__(self,start):
        self.start=start
        # self.single_process()
        # self.multiple_process()
        self.map_mul_process()

    def single_process(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            f1=executor.submit(self.msg,2)
            print(f1.result())

    """To use multiple process """
    def multiple_process(self):
        x=[i for i in range(5,0,-1)]
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results=[executor.submit(self.msg,sec) for sec in x]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

        """Map to use multiple process it return results in the order process started !"""
    def map_mul_process(self):
        x=[i for i in range(5,0,-1)]
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results=executor.map(self.msg,x)

        for f in results:
            print(f)

    def msg(self,sec):
        print('Inside msg function')
        time.sleep(sec)
        return f"Done sleeping for {sec} seconds !"

    def __str__(self):
        return f"Program finished in {round(time.perf_counter()-self.start,2)} seconds !"


if __name__=="__main__":
    x=eg(time.perf_counter())
    print(x)