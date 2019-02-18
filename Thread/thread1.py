import multiprocessing
from multiprocessing import Pool
from multiprocessing import Process
import time
import os

def func(msg):
	print("process:",msg," - (", str(os.getpid()), ") START..")
	time.sleep(3)
	print("process",msg," - (", str(os.getpid()), ") END..." )
if __name__=="__main__":
	# start=time.time()
	# p=Pool(processes=3)
	# for i in range(4):
	# 	msg=("applying ", str(i))
	# 	#p.apply_async(func,(msg,))
	# 	p.apply(func,(msg,))
	# p.close()
	# p.join()
	# print("main end...")
	# print(time.time()-start)
	p=0
	for i in range(4):
		msg=("applying ", str(i))
		p=Process(target=func,args=(msg,))
		p.start()
	p.join()
	print("MAIN DONE...")

