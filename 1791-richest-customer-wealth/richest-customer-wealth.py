class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0

        for a in accounts:
            temp_sum = sum(a)
            if(temp_sum > result):
                result = temp_sum

                
        return result

