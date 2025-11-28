from collections import deque
from typing import List


class Solution:
    def move_clockwise(self,c:str) -> str:
        return '0' if c=='9' else chr(ord(c)+1)
    def move_anti_clockwise(self,c:str) -> str:
        return '9' if c=='0' else chr(ord(c)-1)
    def getAllPair(self,s:str)->List[str]:
        res=[]
        arr=list(s)

        for i in range(4):
            original= arr[i]
            temp1= arr[:]
            temp1[i]=self.move_clockwise(original)
            res.append("".join(temp1))
            temp2= arr[:]
            temp2[i]=self.move_anti_clockwise(original)
            res.append("".join(temp2))
        return res


    def openLock(self, deadends: List[str], target: str) -> int:
        dead= set(deadends)
        if "0000" in dead:
            return -1


        queue= deque(["0000"])
        visited={"0000"}
        steps=0

        while queue:
            for _ in range(len(queue)):
                curr=queue.popleft()
                if curr == target:
                    return steps
                if curr in dead:
                    continue
                for pair in self.getAllPair(curr):
                    if pair not in visited and pair not in dead:
                        queue.append(pair)
                        visited.add(pair)
            steps += 1
        return -1




#How to define queue in python?
# queue= deque()
#Adding element x to the queue
#queue.append(x)
#How to defined HashSet(HashSet)
# HashSet=set()
#Adding element x to the set
#HashSet.add(x)
#How to defined List<String> list in python
# list=[]
#How to define stringbuilder in python str, orignal string= s
# str=s[:]--> creates a empty [0,0,0,0]
# for _ in range(len(queue)):



