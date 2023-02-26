def maximum_weighted_independent_set(G, w):
    n = len(G)
    A = [0] * (n + 1)
    A[1] = w[1]
    
    for i in range(2, n + 1):
        A[i] = max(A[i - 1], A[i - 2] + w[i])
    
    S = set()
    i = n
    
    while i >= 1:
        if A[i - 1] >= A[i - 2] + w[i]:
            i -= 1
        else:
            S.add(i)
            i -= 2
    
    return S
