hour = int(input("Enter the number our hours "))
minutes = int(input("Enter the number our minutes "))
seconds = int(input("Enter the number our seconds"))

total_seconds = (hour * 3600) + (minutes * 60) + seconds

print(f'The total number of  seconds: {total_seconds}')