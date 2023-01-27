class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        number = 0
        for num in data:
            if number == 0:
                if num >> 7 == 0: #1bytes
                    continue
                elif num >> 5 == int('110', 2): #2bytes
                    number = 1
                elif num >> 4 == int('1110', 2): #3bytes
                    number = 2
                elif num >> 3 == int('11110', 2): #4bytes
                    number = 3
                else:
                    return False
            else:
                if num >> 6 == int('10', 2):
                    number -= 1
                else:
                    return False

        return True if number == 0 else False
