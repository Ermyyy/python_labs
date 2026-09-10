n = int(input('A: '))
t = 0
k = 0
for x in range(n):
    s = input(f'in_{x+1}: ').split()
    if len(s) != 4:
        continue
    surename, name, age, study = s
    if study == 'True':
        t += 1
    else:
        k += 1
print(t, k)