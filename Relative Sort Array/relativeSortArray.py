class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        out = []
        for value in arr2:
            for j in range(len(arr1)):
                if arr1[j] == value:
                    out.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for value in arr1:
            if value != -1:
                out.append(value)
        return out
    
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        out = []
       
        for x in arr2:
            while x in arr1:
                out.append(x)
                arr1.remove(x)
        return (out + sorted(arr1))
    

sol = Solution()


# Example 1: Output: [2,2,2,1,4,3,3,9,6,7,19]

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(sol.relativeSortArray(arr1, arr2))
# Example 2: Output: [22,28,8,6,17,44]

arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(sol.relativeSortArray(arr1, arr2))
