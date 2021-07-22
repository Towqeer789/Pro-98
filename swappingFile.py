def swapFileData():
    swap1 = input("Enter Name Swap:-  ")
    swap2 = input("Enter Name Swap:-  ")

    with open(swap1, 'r') as a:
     data_a = a.read()

    with open(swap2, 'r') as b:
     data_b = b.read()

    with open(swap1, 'w') as a:
     a.write(data_b)

    with open(swap2, 'w') as b:
     b.write(data_a)
     
     
print()
# Title of the project
print('Swapping File Data - Project')
# Develpoed details
print('This project is developed by J AJITESH')
print()
#Call the function to execute the program

swapFileData()

print()
# Confirmation Message and thank the user.
print("Data Swapped Successfully")
print()
print("Thank you for using Swapping File Data")
# Helps to re-run the project
print("Run the terminal again to reswap the data in the files.")