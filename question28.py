"""
Possible Number of decodings
Let 'A' represents 1, 'B' represents 2, and so on.
Input : 321
Output : 2
3   21  = c u
3   2   1  = c b  a
"""
def countDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)

    dp[0] = 1  # Empty string has one decoding

    if s[0] == '0':
        return 0  # Invalid encoding

    dp[1] = 1  # Single digit has one decoding

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# Example usage:
input_string = "321"
possible_decodings = countDecodings(input_string)
print("Possible Number of Decodings:", possible_decodings)
