import os
ls = [i for i in os.listdir() if i.endswith('.txt')]
ls.sort()
with open('result.txt','w', encoding='utf-8') as f:
    for j in ls:
        s = open((j),encoding='utf-8').read()
        print(s)
        f.write(s)
        f.write('\n')
