class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:]=zip(*matrix[::-1])
#zip function is used in tuples it return the transpose of the reversed matrix which can be used to rotate image by 90 degree.
