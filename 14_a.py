from math import pi
def fact(a):
    n=1
    for i in range(1,a+1):
        n*=i
    return n 

def sin(num,b):
    ans=0
    num*=(pi/180)
    for i in range(1,b+1,2):
        if i%2==0:
            ans-=((num**i)/fact(i))
        else:
            ans+=((num**i)/fact(i))
    return ans


Sin = lambda x,n: (-1**n) * (((x*(pi/180))**((2*n)+1))/fact((2*n)+1))

def SIN(a,b):
    ans=0
    for i in range(b):
        ans-=Sin(a,i)
    return ans

number    = int(input("Enter a number : "))
itrations = int(input("Enter the number of itrations : "))

print("sin(%.2f) = %.4f \nfound with %.2f number of itreations" % (number,SIN(number,itrations),itrations))

