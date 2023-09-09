def MehediHasan():
    username = input("Enter name: ")
    address = input("Enter address: ")
    mobile = input("Enter mobile: ")
    age = input("Enter age: ")
    about ={
        'Name': username,
        'Address': address,
        'Mobile' : mobile,
        'Age' : age
    }
    print('My name is', about["Name"],', ', 'I live in ', about["Address"],'. ', 'You may contact with me', about["Mobile"], 'And I am', about["Age"], 'years old.')
MehediHasan()





# about ={
#         'Name': 'Mehedi',
#         'Address': 'Dhaka, Bangladesh',
#         'Mobile' : '01977393811',
#         'Age' : '15'
#     }
#     print(about)

    # print("My name is: " + username)
    # print("My address is: " + address)
    # print("My address is: " + mobile)
    # print("My address is: " + age)