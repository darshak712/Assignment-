#Enter a number to program and get the output "Prime" or "Not Prime"
num=int(input("enter the no to check prime or not "))
count=0
i=1
while(i<=num):
    if(num %i)==0:
        count=count+1
    i=i+1
if(count==2):
    print("no is prime")
else:
    print("no is not prime or no is composite number")
"""Output
enter the no to check prime or not 5
no is prime
"""