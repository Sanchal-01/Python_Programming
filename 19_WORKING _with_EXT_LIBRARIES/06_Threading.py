import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(1)  # For waiting and simulating something is happening
    print(f"Thread {num}: Finished")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))  # Here the args is for {num} we have defined as the parameter of the worker function above.
    threads.append(thread) # After a particular thread suppose 0 accepted as argument put the value of thread into [  ].
    thread.start()

for thread in threads:
    thread.join()      # Wait for all threads to finish

print("All threads completed.")