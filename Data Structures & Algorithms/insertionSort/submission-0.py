# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of Insertion Sort
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []  # To store the intermediate states of the array
        
        for i in range(n):
            j = i - 1 #receive the previous index for compare then 

            # Move elements that are greater than key one position ahead - this line executes 
            #if exists an index previous the current
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1 # this return the j index to default position, for interate in list of tuples again
            
            # Clone and save the entire state of the array at this point
            #store the ordened list into a res = [] list, use append for that
            res.append(pairs[:])

        return res #return the ordened array if the while loop returns false more once time