# 4. Take a list from user, the list contain your Mobile Number and find out the Even Numbers List and Odd Number List.
list =[]
even = []
odd = []
for i in range(11):
    i =  int(input('Enter index {}: '.format(i+1)))
    list.append(i)
print('Your Number is: ', list)

def evenList(e):
    for i in e:
        if i%2==0:
            even.append(i)
    print(even)
evenList(list)

def oddList(e):
    for i in e:
        if i%2!=0:
            odd.append(i)
    print(odd)
oddList(list)






# evenList(list)

# def oddList(o):
#     if o%2==1:
#         print('Odd number is: ', oddList(list))