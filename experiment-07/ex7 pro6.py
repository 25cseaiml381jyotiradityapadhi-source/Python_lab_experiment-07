arr = list(map(int, input("Enter integers separated by spaces: ").split()))

positive = sum(map(lambda x: x > 0, arr))
negative = sum(map(lambda x: x < 0, arr))
zero = sum(map(lambda x: x == 0, arr))

n = len(arr)

print("Ratio of positive numbers:", positive / n)
print("Ratio of negative numbers:", negative / n)
print("Ratio of zeros:", zero / n)
