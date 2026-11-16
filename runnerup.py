# Task 3: Runner-up Score
# Name: Pulkit Sharma
# URN: 2481135

n = int(input())
scores = list(map(int, input().split()))

scores = sorted(set(scores))

print(scores[-2])