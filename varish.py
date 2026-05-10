# palindrome program using recursion

def is_palindrome(n, temp, rev=0):
    if n == 0:
        if temp == rev:
            return "the number is a palindrome"
        else:
            return "the number is not a palindrome"
        
    else:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        return is_palindrome(n, temp, rev)
n = int(input("enter a number : "))
result = is_palindrome(n,n)
print(result)      




   

        
