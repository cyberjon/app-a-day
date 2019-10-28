count =0
x=0

while True:
    num = int(input("enternumber"))
    if num >0:
        x = x + num 
        count = count +1
  
    if num <0:
        print(x/count)