mx = 0
for i in range(990, 100, -11):
    for j in range(999, 100, -1):
        if (i*j > mx) and (str(i*j) == str(i*j)[::-1]):
            mx = i*j
print(mx)
