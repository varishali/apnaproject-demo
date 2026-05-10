# palindrome program using selicing


def is_palindrome(n):

    num_str = str(n)
    reversed_str = num_str[::-1]
    return num_str == reversed_str
n = int(input("Enter  a number : "))
if is_palindrome(n):
    print(n,"is a palindrome number")

else:
    print(n, "is not a palindrome number") 




   

        
