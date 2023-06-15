"""Kebi has to send a secret code S to his boss. He designs a method to encrypt the code using two key values N and M. The formula that he uses to develop the encrypted code is shown below:
(((S^N%10)^M%1000000007)
write an algorithm to help Kebi to encrypt the code
N
M
S
a=pow(s,n)
b=a%10
C
"""
N = int(input())
M = int(input())
S = int(input())

a = pow(S, N)
b = a % 10
C = pow(b, M) % 1000000007

print(C)