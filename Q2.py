# 2. Take a list from user, the list contain your Mobile Number and find out the Max and Min number from the list.
# Create seperate function to find out Max and Min.
userlist =[]
for i in range(11):
    i =  int(input('Enter index {}: '.format(i+1)))
    userlist.append(i)
print('Your Number is: ',userlist)

#Minimum item 
def maxNum():
    print('My maximum number is: ',max(userlist))
maxNum()
def minNum ():
    print('My minimum number is: ',min(userlist))
minNum ()




