first = 1
second = 2
third = first+second
sumx = 2

while third < 4000000:
    if third % 2 == 0:
        sumx += third
    first = second
    second = third
    third = first+second

print(sumx)
