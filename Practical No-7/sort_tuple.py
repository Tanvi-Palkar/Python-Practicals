#program to sort tuple by total digits

def count_d(tup):
    return (sum([len(str(ele)) for ele in tup ]))
list = [(11, 23, 45, 34), (34, 67), (323,), (78, 15, 73, 95), (60, 35)]
print("The list is : ")
print(list)
list.sort(key = count_d)

print("The List after sorted tuples are ")
print(list)
