from typing import List
import heapq


class taskScedular:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_array=[0]*26
        for task in tasks:
            freq_array[ord(task)-ord('A')]+= 1

        max_heap= []
        for i in freq_array:
            if i!=0:
                heapq.heappush(max_heap, -i)
        total_time=0
        windows=n+1


        while len(max_heap)>0:
            remaining_tasks=[]
            time=0
            for window in range(windows):
                if max_heap:
                    most_frequent_element=-heapq.heappop(max_heap)
                    most_frequent_element-= 1
                    if most_frequent_element > 0:
                        remaining_tasks.append(most_frequent_element)
                    time+=1

            for task in remaining_tasks:
                heapq.heappush(max_heap,-task)

            if not max_heap:
                total_time=total_time+time
            else:
                total_time=total_time+windows
        return total_time



#learning
# max heap in python:  heapq.heappush(max_heap, -value)
# heapq.heappop(max_heap)
# define max_heap=[]
# How to define frequencyArray int [] freq_array : freq_array=[0]*26







