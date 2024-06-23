import math, time

N = 3737
A = math.floor(math.sqrt(N)) + 1
B = A**2 - N
try_num = 1

start = time.time()
while True:
    if math.sqrt(B).is_integer():
        end = time.time()
        b = math.sqrt(B)
        a = A 
        p = a + b 
        q = a - b 
        print(f"{N} = {int(p)} x {int(q)}")
        print(f"{try_num} try")
        print(f"{end - start} seconds")
        break
    else:
        A += 1
        B = A**2 - N
        try_num += 1
        
"""
3737 = 101 x 37
8 try
8.106231689453125e-06 seconds
"""
