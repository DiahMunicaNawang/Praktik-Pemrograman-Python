a, b = 0, 1
for i in range(10):
    line = "0 1"
    for j in range(i-1):
        a, b = b, a+b
        line += f" {b}"
    print(line)
