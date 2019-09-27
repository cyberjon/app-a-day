#lotto rumber generator 
import random

lotto = []
lotto_plus1=[]
lotto_plus2=[]


for i in range(0, 6):
    numbers = random.randint(1,47)
    lotto.append(numbers)

for j in range(0, 6):
    numbers = random.randint(1,47)
    lotto_plus1.append(numbers)

for k in range(0, 6):
    numbers = random.randint(1,47)
    lotto_plus2.append(numbers)
    
print(f'Lotto Numbers are:\n {lotto}\n\n Lotto Plus 1 are:\n {lotto_plus1}\n\n Lotto Plus 2 are:\n\n {lotto_plus2}\n')
