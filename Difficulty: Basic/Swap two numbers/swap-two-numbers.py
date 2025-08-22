class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        temp = a
        a = b
        b = temp
        return [a,b]