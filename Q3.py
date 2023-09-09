# 3. Take a list from user, the list contain your Mobile Number and sort the list with ascending order.

userlist =[]
for i in range(11):
    i =  int(input('Enter index {}: '.format(i+1)))
    userlist.append(i)
print('Your Number is: ', userlist)

print('Your sorted number is: ', sorted(userlist))

