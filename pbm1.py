'''
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers
from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
flag = False

def find2Num(list,k):
    global flag
    s = set(list)
    for n in list:
        if (k-n) in s:
            print("True! \nNumbers {} and {} from the list {} add up to {}.".format(n, k-n, list, k))
            flag = True
            return flag

def main():
    list = [10, 15, 3, 7]
    k = 17
#    print("List is {} ".format(list))
    find2Num(list,k)
    if flag == False:
        print("No two numbers in {} add up to {}.".format(list,k))


if __name__ == "__main__":
    main()

    
