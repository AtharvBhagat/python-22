a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

maximum = max(a, b)

while(1):
    if(maximum %a==0 and maximum %b==0):
        print("LCM is:",maximum)
        break
    maximum=maximum+1