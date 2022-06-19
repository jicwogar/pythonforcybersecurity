#script that encripts text using rot13

#prompt for the source message
source_message = input("what is the message to encript or decript? ")
#convert message to lowercase for simplicity
source_message = source_message.lower()
final_message = ""

# loop each letter in source message
for letter in source_message:
    #convert letter to ascii equivalent 
    ascii_num = ord(letter)
    # check to see if alpha numeric (a-z)
    if ascii_num >= 97 and ascii_num <= 122:
        # add 13 to ascii_num to shift it by 13
        new_ascii = ascii_num + 13
        if new_ascii > 122:
            new_ascii = new_ascii - 26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)
#print converted message
print("message has been converted:")
print(final_message)