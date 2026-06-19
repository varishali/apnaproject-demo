password = input("Creat Password : ")

if(
    len(password) >= 8 and
    any(char.isdigit() for char in password) and
    any(char.isupper() for char in password)
):
    print("Strong password ! ")

else:
    print("Weak Password ! ")

