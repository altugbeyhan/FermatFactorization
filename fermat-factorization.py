import math

N = 3737
A = math.floor(math.sqrt(N)) + 1
B = A**2 - N

while True:
    if math.sqrt(B).is_integer():
        b = math.sqrt(B)
        a = A 
        p = a + b 
        q = a - b 
        print(f"{N} = {int(p)} x {int(q)}")
        break
    else:
        A += 1
        B = A**2 - N
        
# Output: 3737 = 101 x 37     
