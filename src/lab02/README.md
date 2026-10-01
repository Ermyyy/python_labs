# Лабораторная работа №2

## Коллекции и матрицы

---

## Задание A

### min_max

Функция возвращает минимальный и максимальный элементы списка и есть проверка на пустое значение.

```python
def min_max(nums):
    if not nums:
        raise ValueError

    mn = nums[0]
    mx = nums[0]

    for x in nums:
        if x < mn:
            mn = x

        if x > mx:
            mx = x

    return mn, mx
```

![arrays](../../images/lab02/arrays1.png)

### unique_sorted

Функция удаляет повторяющиеся элементы и возвращает отсортированный список.

```python
def unique_sorted(nums):
    res = list(set(nums))
    for i in range(len(res)):
        for j in range(len(res)-1):
            if res[j] > res[j+1]:
                t = res[j]
                res[j] = res[j+1]
                res[j+1] = t
    return res

```

![arrays](../../images/lab02/arrays2.png)

### flatten

Образует список с списками/кортежами в один, есть проверка на тайп еррор.

```python
def flatten(mat: list[list | tuple]) -> list:
    res = []

    for x in mat:
        if type(x) != list and type(x) != tuple:
            raise TypeError

        for el in x:
            res.append(el)

    return res
```

![arrays](../../images/lab02/arrays3.png)

---

## Задание B — matrix.py

### Функция transpose


Для рваной матрицы вызывается ValueError, а так она транспонирует функцию.

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    for x in mat:
        if len(x) != len(mat[0]):
            raise ValueError

    res = []

    for j in range(len(mat[0])):
        newmat = []

        for i in range(len(mat)):
            newmat.append(mat[i][j])

        res.append(newmat)

    return res
```

![matrix](../../images/lab02/matrix1.png)

### Функция row_sums

Функция находит список сумм элементов каждой строки матрицы.

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    for st in mat:
        if len(st) != len(mat[0]):
            raise ValueError

    res = []

    for st in mat:
        res.append(sum(st))

    return res
```

![matrix](../../images/lab02/matrix2.png)

### Функция col_sums

Функция считает список сумм каждого столбца.

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    for x in mat:
        if len(x) != len(mat[0]):
            raise ValueError

    res = []

    for j in range(len(mat[0])):
        s = 0

        for i in range(len(mat)):
            s += mat[i][j]

        res.append(s)

    return res
```


![matrix](../../images/lab02/matrix3.png)

---

## Задание C — tuples.py

### Функция format_record

Функция получает данные студента в виде фио, группы и гпа. Проверяет правильность введенных данных, убирает лишние пробелы в ФИО и делает из имени и отчества инициалы. GPA выводится с двумя знаками после точки.


```python
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:
        raise TypeError

    if len(rec) != 3:
        raise ValueError

    fio, group, gpa = rec

    if type(fio) != str or type(group) != str:
        raise TypeError

    if type(gpa) != float:
        raise TypeError

    if not fio.strip():
        raise ValueError

    if not group.strip():
        raise ValueError

    part = fio.split()

    if len(part) != 2 and len(part) != 3:
        raise ValueError

    if gpa < 0 or gpa > 5:
        raise ValueError

    surnam = part[0].capitalize()
    init = ''

    for name in part[1:]:
        init += name[0].upper() + '.'

    group = group.strip()
    return f'{surnam} {init}, гр. {group}, GPA {gpa:.2f}'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ")))

```


![tuples](../../images/lab02/tuples.png)