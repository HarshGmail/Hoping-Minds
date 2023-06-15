"""Richest Customer wealth
Input : 
accounts= [[1,5],[7,3],[3,5]]
Output : 10

You are given an m X n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has. A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""
def maximumWealth(accounts):
    max_wealth = 0
    for customer_accounts in accounts:
        wealth = sum(customer_accounts)
        max_wealth = max(max_wealth, wealth)
    return max_wealth

# Example usage
accounts = [[1, 5], [7, 3], [3, 5]]
result = maximumWealth(accounts)
print(result)  # Output: 10
