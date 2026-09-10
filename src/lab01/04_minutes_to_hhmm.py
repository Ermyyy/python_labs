m = int(input('Минуты: '))
minutes = m % 60
hours = m // 60
print(f'{hours}:{minutes:02d}')