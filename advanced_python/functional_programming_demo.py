from functools import reduce

scores = [78, 90, 65, 88, 95]

# map() -> bonus marks add karo
updated_scores = list(map(lambda x: x + 5, scores))
print("Updated Scores:", updated_scores)

# filter() -> 80 se zyada score wale interns
high_scores = list(filter(lambda x: x >= 80, scores))
print("High Scores:", high_scores)

# reduce() -> total score
total_score = reduce(lambda x, y: x + y, scores)
print("Total Score:", total_score)