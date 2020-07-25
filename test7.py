import pnmt
import time

n=int(input("enter num: "))
t=int(input("enter thread num: "))

start_time=time.time()
pnmt.PerfectNumber(n,t)

print("-----%second"%(time.time()-start_time))