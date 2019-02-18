import multiprocessing
from multiprocessing import Pool
import time
import numpy as np



def Cal(n):
	sum=0
	id = (int(multiprocessing.current_process().name.split('-')[1]))
	if(id>11):
		print(id)
	for i in range(n):
		sum+=i*i
	return sum
	
if __name__ == '__main__':
	calCount = 10000
	check = 1001
	
	t1 = time.time()
	
	p=Pool()
	result = p.map(Cal,range(calCount))
	#result = p.starmap(Cal,range(calCount))
	p.close()
	p.join()
	
	print(len(result))
	print('pool spend time: %f' %(time.time()-t1) )
	
	
	
	

