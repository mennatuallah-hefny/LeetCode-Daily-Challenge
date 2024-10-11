"""
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

 

Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
"""
# Time Limit Exceeded 53 / 65 testcases passed
# class Solution(object):
#     def smallestChair(self, times, targetFriend):
#         """
#         :param times: List[List[int]] -> A list of [arrival, leaving] times for each friend
#         :param targetFriend: int -> The index of the target friend for whom we want to find the chair
#         :return: int -> The chair number that targetFriend will sit on
#         """

#         # Store the arrival and leaving times of the target friend
#         target_time = times[targetFriend]

#         # Sort the `times` list based on the arrival time of each friend
#         times.sort()

#         # Number of friends (and therefore number of chairs we need to track)
#         n = len(times)

#         # `chair_time[i]` keeps track of when chair `i` will be free. Initialize all chairs as free at time 0.
#         chair_time = [0] * n

#         # Process each friend's arrival and leaving time in the sorted order
#         for time in times:
#             arrival, leaving = time  # Extract arrival and leaving times for the current friend

#             # Find the first available chair (i.e., where `chair_time[i]` <= arrival time)
#             for i in range(n):
#                 if chair_time[i] <= arrival:
#                     # Assign this chair `i` to the current friend and update the time when this chair will be free (i.e., their leaving time)
#                     chair_time[i] = leaving

#                     # If this friend is the target friend, return the chair number `i`
#                     if time == target_time:
#                         return i
#                     break




import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
    
        # Add an index to track which friend is which
        times_with_index = [(times[i][0], times[i][1], i) for i in range(n)]
        # Sort friends by their arrival time
        times_with_index.sort(key=lambda x: x[0])
        
        # Priority queue for available chairs (starting with 0, 1, 2, ..., n-1)
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        
        # Priority queue for currently occupied chairs: (leave_time, chair_number)
        occupied_chairs = []
        
        for arrival, leaving, friend in times_with_index:
            # Free any chairs from friends who have already left
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                leave_time, chair_number = heapq.heappop(occupied_chairs)
                # Add the chair back to the available chairs
                heapq.heappush(available_chairs, chair_number)
            
            # Assign the smallest available chair to the current friend
            assigned_chair = heapq.heappop(available_chairs)
            
            # If this is the target friend, return the chair number
            if friend == targetFriend:
                return assigned_chair
            
            # Mark the chair as occupied until the friend leaves
            heapq.heappush(occupied_chairs, (leaving, assigned_chair))

sol = Solution()
# Example 1: Output: 1
times = [[1,4],[2,3],[4,6]]
targetFriend = 1

print(sol.smallestChair(times=times, targetFriend=targetFriend))

# Example 1: Output: 1
times = [[1,4],[2,3],[4,6]]
targetFriend = 1

print(sol.smallestChair(times=times, targetFriend=targetFriend))