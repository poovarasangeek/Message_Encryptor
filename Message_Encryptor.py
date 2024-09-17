def str_to_binary_convertor(string):
    binary_str=""
    for i in string:
        unicode=ord(i)
        binary=bin(unicode)
        binary_str+=binary[2:]+" "
    print("\nHere this is your encrypted message:\n",binary_str)
    
print("This is a program to encrypt the original messege to binary message\n")    
user_input=input("Please Enter Your Message:\n") 
str_to_binary_convertor(user_input)