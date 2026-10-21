class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        result = 0

        leftMax = height[l]
        rightMax = height[r]
        l += 1
        r -= 1

        while l < r:
            if leftMax <= rightMax:
                rain = leftMax - height[l]
                if rain < 0:
                    rain = 0
                result += rain
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                rain = rightMax - height[r]
                if rain < 0:
                    rain = 0
                result += rain
                rightMax = max(rightMax, height[r])
                r -=1

        if leftMax < rightMax:
            rain = leftMax - height[l]
            if rain < 0:
                rain = 0
            result += rain
        else:
            rain = rightMax - height[r]
            if rain < 0:
                rain = 0
            result += rain

        return result


