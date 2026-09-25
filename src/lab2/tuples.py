def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:
        raise TypeError

    if len(rec) != 3:
        raise ValueError

    fio, group, gpa = rec

    if type(fio) != str or type(group) != str:
        raise TypeError

    if type(gpa) != float and type(gpa) != int:
        raise TypeError

    part = fio.split()

    if len(part) != 2 and len(part) != 3:
        raise ValueError

    if not group.strip():
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
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))