src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique_src.add(num)
    else:
        unique_src.discard(num)
    tmp.add(num)
unique_src_ord = [num for num in src if num in unique_src]
print(unique_src_ord)
