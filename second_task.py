def counting(N: int, K: int) -> int: #СЧИТАЛОЧКА
    original_list = [i+1 for i in range(N)]
    copied_list = original_list.copy()

    while len(original_list) > 1:
        if K > len(original_list):
            link = K % len(original_list)
        else:
            link = K
        print("original_list: --->", original_list)
        print(link, original_list[link - 1])
        del original_list[link - 1]

    last = original_list[0]
    index = None

    for i in range(len(copied_list)):
        if last == copied_list[i]:
            index = i
            break
    return index

if __name__ == "__main__":
    print(counting(3, 7))
