n = [2,89,0,77]
target=91
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==target:
            print("The pairs are:",n[i],n[j])
