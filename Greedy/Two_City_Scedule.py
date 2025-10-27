from typing import List


class twocityscedular:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #sort the array by b-a
        #simple python lambda function
        # f=lambda x,y:x+y
        # f(2,3): lambda function always returns function not int or something

        total_cost=0
        costs.sort(key=lambda x:x[1]-x[0])
        total= len(costs)
        for i in range(total // 2):
            total_cost=total_cost+costs[i][1]
        for i in range(total // 2,total):
            total_cost=total_cost+costs[i][0]


        return total_cost



