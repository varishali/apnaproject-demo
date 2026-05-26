import numpy as np
chars = np.array(list("abcdefghijklmnopqrstuvwxyz1234567890"))

password = ""
for i in range(10):
    password += np.random.choice(chars)

print("Password : ",password)    
