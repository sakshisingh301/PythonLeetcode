import heapq
from typing import List
from collections import Counter

class HandOfStraight:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            # Build group starting from "first"
            for x in range(first, first + groupSize):
                if count[x] == 0:
                    return False

                count[x] -= 1

                if count[x] == 0:
                    # If it's the smallest key, pop from heap
                    if x == minHeap[0]:
                        heapq.heappop(minHeap)
                    else:
                        # Remove from Counter only
                        count.pop(x)

        return True


# ⭐ MAIN FUNCTION
def main():
    obj = HandOfStraight()

    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3

    result = obj.isNStraightHand(hand, groupSize)
    print("Result:", result)


# Run main if file executed directly
if __name__ == "__main__":
    main()
