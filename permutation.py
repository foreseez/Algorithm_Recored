"""
数字的全排列
"""

def permutation(array,low,high):
    if (low >= high):
        print(array)
    else:
        for i in range(low,high+1):
            array[low],array[i] = array[i],array[low]
            permutation(array,low+1,high)
            array[i],array[low] = array[low],array[i]

array = [1,2,3,4]
string = ['a','b','c','d']
permutation(array,0,3)
# permutation(string,0,3)
