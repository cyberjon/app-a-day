from time import time,ctime


t = time()
print(ctime(t))
year=int(ctime(t)[-4:])
bday=input("dd/mm/yy:")
bd = int(bday[-4:])


age = year-bd

if age > 17 :
    print("You Can drive")
