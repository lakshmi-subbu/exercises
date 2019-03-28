from  functools import reduce

listnumbers = [12,23,34,45,56,67,78,89,91]
#1. Program for sum of all items in thelist
b = [reduce(lambda x,y:x+y, listnumbers)]
print(b)
#2. Program for multiplies of all items in the llist
print(reduce(lambda x,y:x*y, listnumbers))
#3. Program for finging the biggest number in the list
print(reduce(lambda x,y:x if x>y else y,listnumbers))
#4. Program for finding the smallest number in the list
print(reduce(lambda x,y: x if x < y else y,listnumbers))
#5. Program for removing duplicates in the list
c = [ 12, 23, 33]
[c.append(i) for i in listnumbers if i not in c]
print(c)
#6. Program for copy of list
g = []
[g.append(i) for i in listnumbers]
print(g)
# Program to find the list of words that are longer than n from a given list of words.
listwords =['apple','orange','pomegranate','pineapple','jackfruit']
d = []
d = list(filter(lambda x: (x in listwords) and (len(x)>8),listwords))
print(d)
#8.program to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
#sentence = "the quick brown fox jumps over the lazy dog"


txtsentence = "the quick brown fox jumps over the lazy dog and"
txt =  txtsentence.split(" ")
#e = []
f = [txt for txt in txtsentence.split(" ") if len(txt)>3 ]
print(f)
e = [len(txt) for txt in txtsentence.split(" ") if txt !='the' and len(txt)>2 ]
print(e)
