def max_earnings(earnings, k):
    n = len(earnings)
    
    # If no days to work, the maximum earnings is 0
    if n == 0:
        return 0
    
    # dp[i] represents the maximum earnings we can get up to day i
    dp = [0] * (n + 1)  # dp[0] is day before first day
    
    # Fill the dp array
    for i in range(1, n + 1):
        print('=========')
        print(dp)
        print('---------')
        # Option 1: Don't work on day i
        dp[i] = dp[i - 1]
        
        # Option 2: Work on up to k consecutive days ending at day i
        current_sum = 0
        for j in range(i, max(i - k, 0), -1):  # Loop through up to k days
            print(i, j)
            print('+++++++++')
            current_sum += earnings[j - 1]  # earnings is 0-indexed
            print(f'{current_sum=}')
            print(f'{dp[i]=}')
            print(f'{(dp[j - 2] + current_sum)=}')
            if j > 1:
                dp[i] = max(dp[i], dp[j - 2] + current_sum)  # Take earnings from before the sequence
            else:
                dp[i] = max(dp[i], current_sum)  # No previous days to consider if j == 1
    
    return dp[n]

# Example usage:
earnings1 = [60, 70, 80, 40, 80, 90, 100, 20]
k1 = 3
print(max_earnings(earnings1, k1))  # Output: 480

# earnings2 = [45, 12, 78, 34, 56, 89, 23, 67, 91]
# k2 = 4
# print(max_earnings(earnings2, k2))  # Output: 460
