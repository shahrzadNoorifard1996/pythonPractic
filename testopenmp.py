import  pnom
import time

n=int(input("enter a number : "))
start_time=time.time()
pnom.PerfectNumber(n)

print("-------5s seconds----"%(time.time()-start_time))