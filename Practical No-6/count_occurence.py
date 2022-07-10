#program to count occurence of given word in a given sentence

string = str(input ("Enter any sentence :"))
word = str (input("Enter word to find count of occurence :"))
arr =[]

count =0
arr= string.split(" ")
for i in range (0,len(arr)):
            if (word == arr[i]):
                count = count+1
print("count of the word ", word ," is :", count)
