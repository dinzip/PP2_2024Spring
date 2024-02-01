def unique(l):
    d = []
    for i in l:
        if i not in d: 
            d.append(i)
    return d
if __name__ == "__main__":
    l = list(map(int, input().split()))

    new = unique(l)

    print(new)