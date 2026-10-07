# Longest Common Subsequence (LCS)
# Dynamic Programming

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n], dp


def build_lcs(X, Y, dp):
    i = len(X)
    j = len(Y)

    result = []

    # Reconstruct LCS
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because we built it backwards
    result.reverse()

    return ''.join(result)


# Example
X = "ABCBDAB"
Y = "BDCABA"

length, dp = lcs_length(X, Y)

lcs = build_lcs(X, Y, dp)

print("String 1:", X)
print("String 2:", Y)
print("LCS:", lcs)
print("LCS Length:", length)
