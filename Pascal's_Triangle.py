class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution=[[1]]
        for i in range(1, numRows, 1):
            solution.append([comb(i, j) for j in range(0, i+1, 1)])
        return solution
        
