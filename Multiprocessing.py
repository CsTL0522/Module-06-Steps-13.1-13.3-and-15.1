import multiprocessing
import time
import random
from datetime import datetime

def timer():
    wait_time = random.uniform(0,1)
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now()}")

if __name__ == "__main__":

    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=timer, name=f"Process-{i+1}")
        processes.append(process)
        process.start()

    for process in processes:
        process.join()