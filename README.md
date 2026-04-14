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

1. 이윤서: 2006년 12월 27일
2. 정희원: 2006년 12월 21일
3. 김효린: 2006년 12월 16일
4. 이예은: 2006년 12월 9일
5. 김주영: 2006년 11월 20일
6. 전은빈: 2006년 11월 7일
7. 이하연: 2006년 9월 22일
8. 김우현: 2006년 9월 1일
9. 최윤지: 2006년 8월 30일
10. 유가현: 2006년 8월 22일
