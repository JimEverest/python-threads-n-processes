from multiprocessing import Pool
import time
import os

def func(str):
	print("Pool:",str)
	print('current pid: %d' %(os.getpid()))
	time.sleep(3)
	print('Pool:', str, 'end', '\n')
	
if __name__=="__main__":
	p=Pool(processes=3)
	time1 = time.time()
	for i in range(4):
		msg = "apply %d" %(i)
		p.apply(func,(msg,))
	p.close()
	p.join()
	print("main end.......")
	print(time.time()-time1)
	
	
	