import multiprocessing
from datetime import datetime

def trans(a,size):
    t=datetime.now()
    for i in range(size):
        a[i] = i
        print(a[i])
    print('spent %s' % (datetime.now()-t))

if __name__ == '__main__':
	print('test share memory')
	num = 10
	a = multiprocessing.Array('i', num) # share memory between 2 processes, (int array length:10  def: 0)
	p = multiprocessing.Process(target=trans,args = (a,num))
	p.start()
	p.close()
	p.join()
	print("join over..............")
	for i in range(num):
		print(a[i])