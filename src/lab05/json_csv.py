import json
import csv
from pathlib import Path
def json_to_csv(json_path: str, csv_path: str) -> None:
    p = Path(json_path)
    with p.open('r', encoding='utf-8') as f:
        data = json.load(f)
    if not data or not isinstance(data,list):
        raise ValueError('пустой json или неверный')
    if not all(isinstance(row,dict) for row in data):
        raise ValueError('нет списка')
    keys = set()
    for row in data:
        for key in row:
            keys.add(key)
    fieldnames = sorted(keys)
    out = Path(csv_path)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    p = Path(csv_path)

    with p.open('r', newline='', encoding='utf-8') as f:
        read = csv.DictReader(f)
        rows = list(read)
        if not read.fieldnames or not rows:
            raise ValueError('csv пустой или нет заголовка')
    out = Path(json_path)
    with out.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
if __name__ == '__main__':
    json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')
    csv_to_json("data/lab05/samples/people.csv","data/lab05/out/people_from_csv.json")
    