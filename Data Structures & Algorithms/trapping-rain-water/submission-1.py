class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        sum = 0

        while (left < right):
            if( max_left > max_right ):
                right -= 1
                if (min(max_left, max_right) - height[right]) > 0:
                    sum += min(max_left, max_right) - height[right]
            if( max_left <= max_right ):
                left += 1
                if (min(max_left, max_right) - height[left]) > 0:
                    sum += min(max_left, max_right) - height[left]

            if( height[left] > max_left ):
                max_left = height[left]
            
            if( height[right] > max_right):
                max_right = height[right]

        return sum