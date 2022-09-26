if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'b', 'd', 'l', 'p'}
    B = {'b', 'd', 'e', 'l', 'p', 'x'}
    C = {'k', 'l', 'p', 't'}
    D = {'d', 'k', 'o', 'p', 'q', 'u', 'v'}

    X = (A.difference(B)).intersection(C.union(D))
    print(f'X = {X}')

    AA = U.difference(A)

    Y = (AA.intersection(D)).union(C.difference(B))
    print(f'Y = {Y}')