import time

def timer(func):
    def track():
        start=time.time()
        func()
        end=time.time()
        print("Time:",end-start)

    return track

@timer
def calculate_time():
    time.sleep(2)
calculate_time()