import threading

def threadfunction(int s,int e):
    cdef unsigned int i
    for i in range (s, e):
        if checkperfectnumber(i):
            print(i)

def PerfectNumber(int n,int t):
    cdef unsigned  int i,l,s,e
    l=int(n / t)
    s, e=1,l
    threads=[]
    for i in range(t):
        threads.append(threading.Thread(target=threadfunction,args=(s,e)))
        threads[i].start()
        s+=l
        e+=l

    for thread in threds:
        thread.join()

cdef inline int checkperfectnumber nogil:
    cdef unsigned int k
    cdef unsigned int s
    k=1
    s=0
    while k<n:
        if n%k==0:
            s+=k
        k+=1
    if s==n:
        return 1
    return 0