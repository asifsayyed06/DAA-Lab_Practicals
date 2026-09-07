def min_coins(coins, amount):
    # dp[i] = minimum coins required to make amount i
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# User Input
n = int(input("Enter number of coins: "))

coins = list(map(int, input("Enter coin values: ").split()))

amount = int(input("Enter amount: "))

result = min_coins(coins, amount)

if result == float('inf'):
    print("Change cannot be made.")
else:
    print("Minimum number of coins:", result)
