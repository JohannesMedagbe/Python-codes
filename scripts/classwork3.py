sum=0
while True:
    a=int(input("Enter an integer:"))
    if 0<a<=100:
        sum+=a
    elif a==0:
        break
print(sum)