src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[idx + 1] for idx in range(len(src) - 1) if src[idx] < src[idx + 1])
print(list(result))
