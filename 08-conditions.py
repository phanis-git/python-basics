environment = input("Enter environment name")
is_prod = False
if environment == 'PROD':
    is_prod = True
    print("Environment" , environment ,":" , is_prod)
elif environment != 'PROD':
    is_prod = False
    print("Environment is " , environment )
