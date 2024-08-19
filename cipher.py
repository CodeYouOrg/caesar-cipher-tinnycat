# add your code here

def encrypt(text, shift):
    result = ""
   # Create for loop
    for char in text:
        #Check if upper case 
        if char.isupper():
            # Find position and shift 
            shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
            result += shifted_char
        #Check if lower case 
        if char.islower():
            #Find position and shift
            shifted_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += shifted_char
        else:
            result += char
            
    return result 

#check the above function
text = "python is fun!"
shift = 5
encrypted_text = encrypt(text, shift)
print(f"Encrypted: {encrypted_text}")