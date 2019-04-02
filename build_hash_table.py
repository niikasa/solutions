# fr m4ch1n3

# Define hash table as a list of list
table = [[] for _ in range(10)]

run = "y"

while run == "y":
    key, value = input("\nEnter key and value: ").split()
    key = int(key)
    print("key = {},  value = {}".format(key,value))
    
# Hash function
    def hash_func(x):
        return x%10

    # Insert function
    def insert(table,key,value):
        table[hash_func(key)].append(value)

    insert(table,key,value)
    print(table, "\n")
    

    run = input("Continue? (y/n) ")
