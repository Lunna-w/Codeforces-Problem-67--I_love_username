n = int(input())
performances = list(map(int, input().split()))

amazing = 0
maximum = performances[0]
minimum = performances[0]

for i in range(1, n):
    if performances[i] > maximum:
        maximum = performances[i]
        amazing += 1
    if performances[i] < minimum:
        minimum = performances[i]
        amazing += 1

print(amazing)