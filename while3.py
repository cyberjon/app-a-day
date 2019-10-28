num = int(input("enter number "))
sum_e=0
sum_o=0
for i in range(1, num+1):
    if i%2==0:
        sum_e= sum_e+i
    elif i%2==1:
        sum_o=sum_o+i
    
print(sum_e)
print(sum_o)