def mco(P, i, j):
    if i >= j:
        return 0
    r = float('inf')
    for k in range(i, j):
        m = mco(P, i, k) + mco(P, k+1, j) + P[i-1]*P[k]*P[j]
        r = min(r, m)
    return r


def mco_dp(P):
    n = len(P)
    M = [[0 for _ in range(n)] for _ in range(n)]
    S = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n+1):
        for i in range(0, n-l):
            j = i+l-1
            r = float('inf')
            for k in range(i, j+1):
                m = M[i][k] + M[k+1][j] + P[i]*P[k]*P[j]
                if m < r:
                    r = m
                    S[i+1][j] = k
            M[i][j] = r
    return M, S


def print_optimal_parens(S, i, j):
    if i == j:
        print("A", i+1, sep="", end="")
    else:
        print("(", end="")
        print_optimal_parens(S, i, S[i][j])
        print_optimal_parens(S, S[i][j]+1, j)
        print(")", end="")


def lcs(x, y):
    n = len(x)
    m = len(y)
    M = [[0 for _ in range(m+1)] for _ in range(n+1)]
    S = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n):
        M[i][0] = 0
    for j in range(m):
        M[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, m):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                S[i][j] = "↖"
            elif M[i-1][j] >= M[i][j-1]:
                M[i][j] = M[i-1][j]
                S[i][j] = "↑"
            else:
                M[i][j] = M[i][j-1]
                S[i][j] = "←"
    return M, S


def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":
        print_lcs(b, x, i-1, j-1)
        print(x[i-1], end="")
    elif b[i][j] == "↑":
        print_lcs(b, x, i-1, j)
    else:
        print_lcs(b, x, i, j-1)


"""
print("Optimal parenthesization:")
P = [30, 35, 15, 5, 10, 20]
M, S = mco_dp(P)
print("M:")
for row in M:
    print(row)
print_optimal_parens(S, 0, len(P)-1)
"""

print("Longest common subsequence:")
x = "ABCBDAB"
y = "BDCABA"
M, S = lcs(x, y)

print_lcs(S, x, len(x), len(y))
