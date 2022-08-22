class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        
        max_left = 0
        max_right = len(height) - 1
        
        # 웅덩이가 생길 경우 웅덩이에 담긴 물의 양을 담아놓는 변수
        temp_left = 0
        temp_right = 0
        
        left = 0
        right = len(height) - 1
        
        while left <= right:
            if height[left] >= height[max_left]:
                # 웅덩이가 만들어질 수 있는 경우
                # temp에 담긴 물의 양이 실제 웅덩이가 되므로, result에 더해준다
                max_left = left
                result += temp_left
                temp_left = 0
            else:
                temp_left += (height[max_left] - height[left])
                    
            if height[right] >= height[max_right]:
                # 웅덩이가 만들어질 수 있는 경우
                # temp에 담긴 물의 양이 실제 웅덩이가 되므로, result에 더해준다
                max_right = right
                result += temp_right
                temp_right = 0
            else:
                temp_right += (height[max_right] - height[right])
                    
            if height[max_left] <= height[max_right]:
                # 지금까지 살펴본 것 중, 오른쪽에 max가 있는 경우, 왼쪽에서 오른쪽으로 다가간다
                left += 1
            else:
                # 지금까지 살펴본 것 중, 왼쪽에 max가 있는 경우, 오른쪽에서 왼쪽으로 다가간다
                right -= 1
        
        return result
