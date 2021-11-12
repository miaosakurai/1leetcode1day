import math
class Solution:
    def findComplement(self, num: int) -> int:
        power = math.log(num, 2)
        if power==int(power):
            power += 1
        return 2 ** ceil(power) - 1 - num