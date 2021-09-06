def fun1(a,b=0,*args,**k):
    c=a+b
    print(c)
    print(a,b)
    print(a,b,args)
    print(k)
fun1(10,20)
fun1(10)
fun1(1,2,3,5,4,6,8)
fun1(a="apple",b="bat",c="cat",d="dog",l="lion")

"""
output
30
10 20
10 20 ()
{}
10
10 0
10 0 ()
{}
3
1 2
1 2 (3, 5, 4, 6, 8)
{}
applebat
apple bat
apple bat ()
{'c': 'cat', 'd': 'dog', 'l': 'lion'}

"""