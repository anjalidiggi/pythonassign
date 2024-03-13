def f(x):
    a=''
    for i in x:
        if i not in a:
            a=a+i
    return a
a=input()
K=int(input())
for i in range(len(a)//K):
    print(f(a[K*i:K*(i+1)]))