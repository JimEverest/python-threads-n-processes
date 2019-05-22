import threading
import time

def  first_fn():
    print(threading.currentThread().getName() + " is running...")
    time.sleep(2)
    print(threading.currentThread().getName() + " is Exiting" )
    
def  second_fn():
    print(threading.currentThread().getName() + " is running...")
    time.sleep(2)
    print(threading.currentThread().getName() + " is Exiting" )
    
def  third_fn():
    print(threading.currentThread().getName() + " is running...")
    time.sleep(2)
    print(threading.currentThread().getName() + " is Exiting" )


if __name__=="__main__":
    # print("hey")

    t1=threading.Thread(target=first_fn, name="1st_FN")
    t2=threading.Thread(target=second_fn, name="2nd_FN")
    t3=threading.Thread(target=third_fn, name="3rd_FN")
    t1.start()
    t2.start()
    t3.start()
    t1.join()

# t2.join()
# t3.join()
print ("all done...")