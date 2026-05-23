text ="i am in stanch it solutions company"
word=text.split()
frequency={}
for words in word:
    if words in frequency:
        frequency[words]+=1
    else:
        frequency[words]=1
print(frequency)