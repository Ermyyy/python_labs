import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.

    По умолчанию используется UTF-8.
    Для другой кодировки можно указать encoding="cp1251".

    Если файл не найден, возникает FileNotFoundError.
    Если файл нельзя декодировать, возникает UnicodeDecodeError.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        stolb = len(rows[0])
        for row in rows:
            if len(row) != stolb:
                raise ValueError('Все строки должны иметь одинаковую длину')
    p = Path(path)
    with p.open('w', newline='', encoding='utf-8') as f:
        wr = csv.writer(f)
        if header is not None:
            wr.writerow(header)
        for r in rows:
            wr.writerow(r)

if __name__ == '__main__':
    print(read_text('data/lab04/input.txt', encoding= 'utf-8'))
    print(write_csv([("word","count"),("test",3)], "data/lab04/check.csv"))