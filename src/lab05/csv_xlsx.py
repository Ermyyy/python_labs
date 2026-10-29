
import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    

    p = Path(csv_path)

    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV файл пустой")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        max_len = 0

        for cell in col:
            if cell.value is not None:
                length = len(str(cell.value))
                if length > max_len:
                    max_len = length

        letter = col[0].column_letter
        ws.column_dimensions[letter].width = max(max_len + 2, 8)

    wb.save(xlsx_path)


if __name__ == "__main__":
    csv_to_xlsx(
        "data/lab05/samples/people.csv",
        "data/lab05/out/people.xlsx"
    )
