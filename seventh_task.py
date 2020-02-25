import numpy as np

def counting(data, min, max):
    n = max - min + 1  # [0, n]
    counters = [0] * n

    for v in data:
        counters[v - min] += 1

    result = []
    for v, count in enumerate(counters):
        result.extend([v + min] * count)

    return result

if __name__ == "__main__":
    N = 10**6
    arr = np.random.randint(13, 26, N)

    print("arr[:20] : --->", arr[:20])
    print("counting(data, min, max)[:how many] : --->", counting(arr, 13, 26)[:15])