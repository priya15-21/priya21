L=[(int(input("enter the elements:")))for i in range(int(input("enter the total elements:")))]
for n in range(len(L)-1,-1,-1):
    dup=False
    for j in range (0,n):
        if L[j]==L[n]:
            dup=True
            break
        else:
            j=j+1
    if dup:
        del L[n]
    else:
        n=n+1
print(L)    