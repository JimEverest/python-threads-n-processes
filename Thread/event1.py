import multiprocessing
import time

def wait_for_event(e):
    print("wait for event : start")
    e.wait()
    print("wait for event is_set:" , str(e.is_set()))
    
def wait_for_event_time(e,t):
    print("wait for timeout: starting")
    e.wait(t)
    print("wait for event timeout is_set: ", str(e.is_set()))
    
if __name__ == "__main__":
    e = multiprocessing.Event() # create an event
    w1 = multiprocessing.Process(name='block',target = wait_for_event, args=(e,))
    w2 = multiprocessing.Process(name='non-block', target = wait_for_event_time, args = (e,2))
    
    w1.start()
    w2.start()
    time.sleep(3)
    e.set()
    print("main event is set")
	
	