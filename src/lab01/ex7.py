st = input()
a = []
for x in range(len(st)):
    if st[x].isupper():
        a.append(st[x])
        first = x
        break

for x in range(first+1,len(st)-1):
    if st[x] in '0123456789':
        a.append(st[x+1])
        sec = x+1
        break


step = sec - first
x = step+sec
while x < len(st):
    a.append(st[x])
    if st[x] == '.':
        break
    x += step

print(''.join(a))