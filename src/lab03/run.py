def count_freq(tokens: list[str]) -> dict[str, int]:
    res = {}
    for i in tokens:
        res[i] = res.get(i,0) + 1
    sorted_res = sorted(res.items(), key = lambda i: (i[0], i[1]))
    return dict(sorted_res)


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    c = list(count_freq(freq).items())
    return c[:n]
print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))