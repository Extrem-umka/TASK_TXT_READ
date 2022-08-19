texts = ['1.txt', '2.txt', '3.txt']

dict_r = {}
dict_w = {}

for text in texts:
    with open(text, encoding='utf-8') as f:
        txt = f.read().split('\n')
        s = len(txt)
        dict_r[s] = text
        dict_w[s] = txt

sorted_dict_r = sorted(dict_r.items())
print(sorted_dict_r)

with open('result.txt', 'w', encoding='utf-8') as f:
    for k, v in sorted_dict_r:
        f.write(f'{str(k)}\n{v}\n')
        for text in dict_w[k]:
            f.write(f'{text}\n')
