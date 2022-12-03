lst = [1.4, 1.2, 3.1, 10.011]
remains = []
for i in range(len(lst)):
    remains.append(lst[i] % 1)
print(round(max(remains) - min(remains), 3))
