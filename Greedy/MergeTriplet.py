from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x_found= False
        y_found =False
        z_found= False
        for x,y, z in triplets:
            if x> target[0] or y> target[1] or z> target[2]:
                continue
            if x == target[0]:
                x_found=True
            if y==target[1]:
                y_found=True
            if z ==target[2]:
                z_found=True
        return x_found and y_found and z_found