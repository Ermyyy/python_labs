import argparse
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def freq_txt(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return count_freq(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))

parser = argparse.ArgumentParser()
parser.add_argument("--in",dest="input_path",default="data/lab04/input.txt")
parser.add_argument("--out",dest="output_path",default="data/lab04/report.csv")
parser.add_argument("--encoding", default="utf-8")
argums = parser.parse_args()
try:
    txt = read_text(argums.input_path, encoding=argums.encoding)
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)

freq = freq_txt(txt)
rows = sorted_word_counts(freq)
write_csv(rows, argums.output_path, header=('word', 'count'))


print("Всего слов:", sum(freq.values()))
print("Уникальных слов:", len(freq))
print("Топ-5:")
for word, count in top_n(freq, 5):
    print(f"{word}: {count}")
