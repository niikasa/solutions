# Fix to Bug15 in Pbm1.py

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
    for i in range(len(list)-1):
        if (k-list[i]) in list:
# Continue(skip to next value of i) if number occurs once only and k is
# double that number.            
            if (list.count(k-list[i])==1) and k==(2*list[i]):
                continue
            print("True! \nNumbers {} and {} from the list {} add up to {}.".format(list[i], k-list[i], list, k))
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


