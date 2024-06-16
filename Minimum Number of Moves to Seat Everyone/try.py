seats = [3,1,5]
students = [2,7,4]
# Output: 4

students.sort()
seats.sort()
min_moves = 0
for i in range(0, len(seats)):
    min_moves += abs(seats[i] - students[i])


print(min_moves)