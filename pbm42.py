'''
Daily Coding Problem: Problem #42

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that
returns a subset of S that adds up to k. If such a subset cannot be made,
then return null.

Integers can appear more than once in the list. You may assume all numbers
in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
since it sums up to 24.

'''

ansSubArr = None
def iterSubArr(arr, subArr, target, index):
    global ansSubArr
    if sum(subArr) == target:
        ansSubArr = subArr
        return

    if ansSubArr or sum(subArr)>target:
        return

    if index < len(arr):
        iterSubArr(arr, subArr+[arr[index]],target, index+1)
        iterSubArr(arr, subArr,target, index+1)


def subArr(arr, target):
    iterSubArr(arr, [], target, 0)
    return ansSubArr


def main():
    arr = [1, 12, 1, 61, 5, 9, 2]
    target = 26
    print('Subset of {} that adds up to {} is {}'.format(arr,target,subArr(arr,target)))


'''
Special variable __name__ is set to '__main__' if subarray-sum.py is directly
executed.
If subarray-sum.py is imported, special variable __name__ is not populated.
'''
if __name__ == '__main__':
    main()
    

