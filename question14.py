"""
int BalanceFruits(int a, int m, int rs):

You have a basket full of apples and mangoes, your job is to make the numer of apples and given a function that accepts three integers 'a'. 'm' and rsas its argument where 'a' and a basket respectively and 'rs' is the rupees that you have. Implement the function to balance the basket.

1 * f' * a' >^ prime m^ prime . then buy (a-m) mangoes at the rate of Rs 1 per mango. If 'a'<'m'. then sell (m- a) mangoes at the rate of Rs 1 per mangoReturn the total/rupees left with you after balancing the fruits.

Assumption:

1 >= 0 m >= 0 and rs >= 0 rs >= (a - m)

Note: If a = m return rs unchanged

Sample Input:

a:8

m:4

rs:6

Sample Output:
2
"""

def BalanceFruits(a, m, rs):
    if a == m:
        return rs
    elif a > m:
        return rs + (a - m)
    else:
        return rs - (m - a)

# Example usage:
a = 8
m = 4
rs = 6

result = BalanceFruits(a, m, rs)
print("Total rupees left after balancing the fruits:", result)
