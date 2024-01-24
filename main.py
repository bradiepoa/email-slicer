while True:
    # creating a variable
    email = input('Enter an email to slice: ')
    
    # finding an index, letter you want
    # print(email.index('@'))
    
    if email.count('@') == 1 and len(email[:email.index('@')]) > 0 and len(email[email.index('@')+1:]) > 0:
        print("Your username is : " + email[:email.index('@')])
        print("And your domain name is : " + email[email.index('@')+1:])
    else:
        print('Invalid email')
