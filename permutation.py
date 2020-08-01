"""
数字的全排列
"""
res = []
def permutation(array,low,high):
    # res = []
    if (low >= high):
        # res = []
        num = [str(i) for i in array]
        res.append("".join(num))
        # print(res)
        # return res
        # print(array)
    else:
        for i in range(low,high+1):
            array[low],array[i] = array[i],array[low]
            permutation(array,low+1,high)
            array[i],array[low] = array[low],array[i]

array = [1,2,3,4]
string = ['a','b','c','d']
permutation(array,0,3)
print(res)
ans = 0
for i in res:
    num = eval(i)
    if num % 7==0:
        ans += 1

print(ans)
# permutation(string,0,3)

#
# def permutation(array,low,high):
#     res = []
#     if (low>=high):
#
