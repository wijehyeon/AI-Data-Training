from typing import List


class Solution:
	def __init__(self):
		self.trap([0,1,0,2,1,0,1,3,2,1,2,1])
		
	def trap(self, height: List[int]) -> int:
		stack = []
		volume = 0
		for i in range(len(height)):
			while stack and height[i] > height[stack[-1]]:
				print(stack)
				top = stack.pop()
				print('stack head out')
				if not len(stack):
					break
				print(f'i={i}, stack[-1]={stack[-1]}')
				distance = i - stack[-1] - 1
				waters = min(height[i], height[stack[-1]]) - height[top]
				print(f'height[top]:{height[top]}')
				print(f'distance:{distance} and waters:{waters}')
				volume += distance * waters
				print(f'volume added +{volume}')
			stack.append(i)
			print('==========')
		return volume
	
Solution()
