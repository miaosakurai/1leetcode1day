class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ix1 = max(ax1, bx1)
        ix2 = min(ax2, bx2)
        iy1 = max(ay1, by1)
        iy2 = min(ay2, by2)
        i = max(0, (ix2-ix1)) * max(0, (iy2-iy1))
        return (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) - i