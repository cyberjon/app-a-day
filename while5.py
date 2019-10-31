count =1
start=0
num= int(input("enternumber"))
x=0
sum_e=0
sum_o=0
while x in range(x,num) :
    
    if x%2==0:
        sum_e =sum_e+x
        x = x+1
        
    if x%2!=0:
        sum_o =sum_o+x
        x = x+1
print(sum_e)    
print(sum_o)      