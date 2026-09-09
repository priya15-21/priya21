s = input("Enter a string: ")
vowels = []
      
for a in s:
        if a in "aeiouAEIOU":
            vowels.append(a)
a=[]            

for i in s:
    if i in "aeiouAEIOU":
        a.append(vowels.pop())
    else:
        a.append(i)

print(''.join(a))