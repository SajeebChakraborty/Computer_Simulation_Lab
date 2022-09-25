def LCM(x0,a,c,m,r_num,n):
        r_num[0]=x0
        for i in range(1,n):
            r_num[i]=((r_num[i-1]*a)+c)%m

if __name__ == "__main__":
    x0=27
    a=127
    c=43
    m=100
    n=10

    r_num=[0]*n
    LCM(x0,a,c,m,r_num,n)

for i in range(n):
    print(r_num[i],end = " ")


dup={x for x in r_num if r_num.count(x)>1}
print(r_num)
print("\n")

print(dup)
print(len(dup))