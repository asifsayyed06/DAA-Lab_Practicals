def matrix_chain_order(p):
    n = len(p) - 1

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            # Set initial value to infinity
            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# Matrix dimensions
# A1 = 10 x 20
# A2 = 20 x 30
# A3 = 30 x 40

p = [10, 20, 30, 40]

minimum_cost = matrix_chain_order(p)

print("Minimum number of multiplications:", minimum_cost)
