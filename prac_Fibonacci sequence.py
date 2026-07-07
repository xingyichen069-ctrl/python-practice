#函数返回第n个斐波那契数
def n_fib(n):
    if n==0:return 1
    if n==1:return 1
    else:return n_fib(n-1)+n_fib(n-2)

n= int(input("Please input the position of your wanted number: "))
print(f"Your wanted number is: {n_fib(n)}")

