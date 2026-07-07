def gcd(a,b):
    #计算最大公约数
    if(a<b):a,b=b,a

    r=a%b
    if(r==0):return b
    else:
        while(r>0):
            a,b=b,r
            r=a%b
            if(r==0):return b

a=int(input("请输入数字一："))
b=int(input("请输入数字二："))

print(f"最大公约数gcd为：{gcd(a,b)}")
print(f"最小公倍数lcm为：{int(a*b/gcd(a,b))}")

#or:

def k_fib(k):
    a,b=1,1
    for i in range(k-1):
        a,b = b,a+b
        return a

n= int(input("Please input the position of your wanted number: "))
print(f"Your wanted number is: {k_fib(n)}")
