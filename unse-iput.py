# list and find the sum of all integers
list = [2, 3, 5, 6, 8]
print(type(list))
result=sum(list)
print(result)

#establish a tuple of the book you love and create a loop
MyBooks=('Rich and poor Dad', 'My life my purpose my potential', 'the secret', 'Grow and Think Rich', 'The way of a Superior Man')
for book in MyBooks:
 print(book)

 #a disctionary of personal information
 Personal_info={'name':'Daud', 'Age':'13', 'favourite color':'black'}
 print(Personal_info)

 #create a two sets and establish a set oof which intergers are common
 set1={2,3,4,5,6,7,8}
 set2={8,9,4,3,10}
 set1&set2
 print(set1&set2)

 #a list of words and create a comprehension
 numbers=[number*number for number in range(2,5)]
 print(numbers)
 words=['p','t','r','p','r','k' in range(1,4)]
 print(words)