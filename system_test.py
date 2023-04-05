def count_bits(n):
    if n == 0:
        return 0
    else:
        div = 2
        remainder = n % div
        return remainder + 10 * count_bits(n // 2)

print(count_bits(100))


