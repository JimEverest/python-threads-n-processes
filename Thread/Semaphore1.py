import multiprocessing
import time


def consumer(s):
    s.acquire()
    print(multiprocessing.current_process().name + ' get...')
    time.sleep(1)
    s.release()
    print(multiprocessing.current_process().name+ ' release')
	

	
	
if __name__ == '__main__':
    s = multiprocessing.Semaphore(3)
    for i in range(5):
        p = multiprocessing.Process(target=consumer,args=(s,))
        p.start()
    print(multiprocessing.current_process().pid , ' ...  main end')
	
	
	
	
