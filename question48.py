"""n=5, k=2, a[]={5,3,2,1,4}
Output :
2

A company decide to hire some candidates. They arrange a JOB INTERVIEW to hire them. If total N candidates apply for the JOB, you have to select K candidates for the INTERVIEW from the total number of candidates. You can select the K candidates for the interview according to their academic scores. If all the candidates have the same score then call all the candidates for an interview.
"""
def getMinimumScore(N, K, a):
    a.sort()  # Sort the array in non-decreasing order

    if a[0] == a[N-1]:
        return a[0]  # All candidates have the same score
    else:
        return a[K-1]  # Return the score of the Kth candidate

# Example usage
N = 5
K = 2
a = [5, 3, 2, 1, 4]
minimum_score = getMinimumScore(N, K, a)
print(minimum_score)  # Output: 2
