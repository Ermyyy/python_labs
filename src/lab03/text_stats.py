import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.readline()


text = normalize(text)


tokens = tokenize(text)


freq = count_freq(tokens)
top = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for w, c in top:
    print(f"{w}:{c}")