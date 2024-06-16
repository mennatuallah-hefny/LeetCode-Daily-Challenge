class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        seats.sort()
        min_moves = 0
        for i in range(0, len(seats)):
            min_moves += abs(seats[i] - students[i])
        return min_moves
    
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        min_moves = sum([abs(x-y) for x,y in zip(seats,students)])
        
        return min_moves