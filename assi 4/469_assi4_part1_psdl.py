#tuple 1
tup1=("java", "python", "c++", "react.js", "sql")
#print the tuple
print(tup1)
#searching for a word in the tuple
word=input("enter the word to search in the tuple: ")
if word in tup1:
    print(f"{word} is found in the tuple")
else:
    print("word not found")
#tuple 2
tup2=("physics", "chemistry", "maths", "biology")
#concatenate tuples
#method - 1
res=tup1+tup2
print(res)
#method - 2
res=sum((tup1, tup2), ())
print(res)
#method - 3
x=list(tup1)
y=list(tup2)
x.extend(y)
res=tuple(x)
print(res)
#convert tuple items to a single string
res=" ".join(tup1)
print(res)
#deleting a tuple
del tup2
print("tuple two was deleted successfully")
#converting list to a tupe
lst=[]
n=int(input("enter the number of elements in the list: "))
for i in range(n):
    ele=input("enter the element to be entered in the list: ")
    lst.append(ele)
#method - 1
list_to_tuple1=tuple(lst)
#method - 2
def list_to_tuple_function(lst):
    result=()
    for item in lst:
        result+=(item, )
    return result
print(list_to_tuple_function(lst))
#method - 3: using recursion
def list_to_tuple_recur(lst, index=0):
    if(index==len(lst)):
        return ()
    return (lst[index],) + list_to_tuple_recur(lst, index+1)
print(list_to_tuple_recur(lst))

'''
('java', 'python', 'c++', 'react.js', 'sql')
enter the word to search in the tuple: java
java is found in the tuple
('java', 'python', 'c++', 'react.js', 'sql', 'physics', 'chemistry', 'maths', 'biology')
('java', 'python', 'c++', 'react.js', 'sql', 'physics', 'chemistry', 'maths', 'biology')
('java', 'python', 'c++', 'react.js', 'sql', 'physics', 'chemistry', 'maths', 'biology')
java python c++ react.js sql
tuple two was deleted successfully
enter the number of elements in the list: 4
enter the element to be entered in the list: 34
enter the element to be entered in the list: 3
enter the element to be entered in the list: 65
enter the element to be entered in the list: 444
('34', '3', '65', '444')
('34', '3', '65', '444')
'''

