def hanoi(n: int, start: int, end: int) -> None:
    if n == 1:
        print(start, "->", end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        print(start, "->", end)
        hanoi(n - 1, other, end)

hanoi(3, 1, 3)