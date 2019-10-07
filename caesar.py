text =input("Enter your sentance: ")
shift = int(input("Enter the shift key:"))

cipher_text=''
for c in text:
    cipher_text += chr((ord(c) + shift))
    

    
print(cipher_text)



