# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05

2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is 
the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any 
two distinct critical points. 

If there are fewer than two critical points, return [-1, -1].

"""    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def appendAll(self, arr: list):      
      for val in arr:
        self.append(val)
     
class Solution(object):
    def nodesBetweenCriticalPoints(self, head: ListNode):
        
        critical_points = []
        prev = None # set previous to None
        curr = head  # set curr to first node
        idx = 1

        #iterate through the list node
        while curr:
            print(curr.val)
            # if you have a current and next value
            if prev and curr.next:
                # check for min, max
                if (curr.val > prev.val and curr.val > curr.next.val):              
                    critical_points.append(idx)
                elif (curr.val < prev.val and curr.val < curr.next.val):               
                    critical_points.append(idx)
            # increment the index
            idx+=1
            prev = curr
            curr = curr.next    

        # check for requirement
        if len(critical_points) < 2:
            return [-1, -1]

        # set min and max to max values, we will for min an max
        min_diff = float('inf')
        max_diff = float('-inf')
        min_v = 0
        max_v = 0
       
        # debug your crit points 
        for i in range(len(critical_points)):
            print("crit point", critical_points[i])
        
        # loop through the crit points and check all possible differences            
        for i in range(len(critical_points)):
            print ("i", i, critical_points[i])
            for j in range(len(critical_points)):
                # do not check same index
                if i != j :
                    # get the min value using min
                    min_v = min(critical_points[i], critical_points[j])
                    # get the max value using max
                    max_v = max(critical_points[i], critical_points[j])                    
                    diff = max_v - min_v
                    
                    # get the min and max value in each iteration
                    min_diff = min(min_diff, diff)
                    max_diff = max(max_diff, diff)
        
        # print ("*** min_diff", min_diff, "max_diff", max_diff)
        return [min_diff, max_diff]

ll = LinkedList()
ll.appendAll([3,1])
ll.appendAll([5,3,1,2,5,1,2])
ll.appendAll([1,3,2,2,3,2,2,2,7])

result = Solution().nodesBetweenCriticalPoints(ll.head)
print(result)


