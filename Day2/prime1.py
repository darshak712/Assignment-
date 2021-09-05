#Write a program to find the prime number
lower=int(input("enter the no "))
upper=int(input("enter the no "))
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
"""Output
enter the no 1
enter the no 5
2
3
5
"""