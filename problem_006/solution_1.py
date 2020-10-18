"""
Problem 6: https://projecteuler.net/problem=6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def solution():
    sum_sq = 0
    for i in range(1,101):
        sum_sq += i
    sum_sq **=2
    sq_sum = 0
    for j in range(1,101):
        sq_sum += j**2
    return (sum_sq-sq_sum)

print(solution())