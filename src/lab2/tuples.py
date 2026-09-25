def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    if not fio.strip() and not group.strip():
        raise ValueError
    if type(gpa) != float:
        raise TypeError
    part = fio.split()
    surnam = part[0].capitalize()
    init = ''
    for name in part[1:]:
        init += name[0].upper() + '.'
    group = group.strip()
    return f'{surnam}, гр. {group}, GPA {gpa:.2f}'
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))