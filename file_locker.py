print("\033[1m== SECRET FILE LOCKER ==\033[0m")

password = "12345"
notes = []
attempt = 0

while attempt < 3:
    user_password = input("Enter locker password : ")

    if user_password == password:
        print("\033[1m= LOGIN SUCCESSFULLY =\033[0m")
        
        while True:
            print("\033[1m= FILE LOCKER MENU =\033[0m")
            print("1. Add Secret Note")
            print("2. View Notes")
            print("3. Delete Note")
            print("4. Change Password")
            print("5. Exit")

            choice = input("Enter your choice : ")
            #add note
            if choice == "1":
                note = input("Write your secret note : ")
                notes.append(note)
                print("Secret note save successfully.")
                go_back = input("Do you want to contine ? (yes/no) : ")
                if go_back.lower() != "yes":
                    print("Thanks for using SECRET FLIE LOCKER")
                    break

            #view note
            elif choice == "2":
                if len(notes) == 0:
                    print("No secret notes found.")

                else:
                    print("YOUR SECRET NOTE")

                    for i in notes:
                        print("-",i)

                go_back = input("Do you want to contine ? (yes/no) : ")
                if go_back.lower() != "yes":
                    print("Thanks for using SECRET FLIE LOCKER")
                    break        
            #delete note
            elif choice == "3":
                if len(notes) == 0:
                    print("No notes available.")

                else:
                    print("YOUR NOTES")

                    for i in range(len(notes)):
                        print(f"{i+1}. {notes[i]}")
                    delete = int(input("Enter note number to delete : "))

                    if delete <= len(notes):
                        removed = notes.pop(delete - 1) 
                        print(f"Delete note : {removed}") 

                    else:
                        print("Invalid note number!")

                go_back = input("Do you want to contine ? (yes/no) : ")
                if go_back.lower() != "yes":
                    print("Thanks for using SECRET FLIE LOCKER")
                    break        

            #change password
            elif choice == "4":
                old_password = input("Enter old password : ")
                if old_password == password:
                    new_password = input("Enter new password : ")
                    password = new_password
                    print("Password change successfuly.")

                else:
                    print("Wrong old password!")

                go_back = input("Do you want to contine ? (yes/no) : ")
                if go_back.lower() != "yes":
                    print("Thanks for using SECRET FLIE LOCKER")
                    break    


            #exit
            elif choice == "5":
                print("Thanks for using SECRET FILE LOCKER")
                break
            else:
                print("Invalid chice!")

        break                    
                              
    else:
        attempt += 1

        print(f"WRONG PASSWORD | ATTEMPTs LEFT : {3 - attempt}")

if attempt == 3:
    print("LOCKER BLOCKED FOR SECURITY REASON")        

        
