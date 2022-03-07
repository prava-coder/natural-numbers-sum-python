#write a program to find the sum of natural numbers

num=12
if num<0:
    print("you number should be greater than zero to find the natural numbers")
else:
    sum=0
    #using while to iterate until zero
    while(num>0):
        sum+=num
        num-=1
    print("the sum is",sum)
