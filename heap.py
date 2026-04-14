import pandas as pd
import heapq

df = pd.read_csv('birthday.csv')
df = df.dropna(subset=['생년(예. 1985)', '생월(예. 12)', '생일(예. 5)'])

birthday_heap = []
for _, row in df.iterrows():
    y, m, d = int(row['생년(예. 1985)']), int(row['생월(예. 12)']), int(row['생일(예. 5)'])
    name = row[' ']
    heapq.heappush(birthday_heap, (-y, -m, -d, name))

count = 0
while birthday_heap and count < 10:
    y, m, d, name = heapq.heappop(birthday_heap)
    print(f"{count+1}. {name}: {abs(y)}년 {abs(m)}월 {abs(d)}일")
    count += 1
