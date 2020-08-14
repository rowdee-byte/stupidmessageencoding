import random, time, csv
from datetime import date
#   Seperate the message into an array with each element being a char
#   Create an array with the ASCII values of each char
#   Add or take the key number from the ASCII values
#   Clear the plaintext array to save memory :)
#   New array to store the changed ASCII values as its text counterpart
#   Return the encrypted message

def test(msg):
    return None

def encrypt(msg, keyn, debug):
    plaintext_array = []
    shakes_array = []
    length_of_message = len(msg)

    if debug:
        debug_time1 = time.time()

    for i in range(0, length_of_message): 
        plaintext_array.append(msg[i])

    if debug:
        debug_time2 = time.time()
        totalt = debug_time2 - debug_time1
        num = str(totalt)
        i = num.index(".")
        truncated = num[:i + 4]
        print(f"\nDEBUG: Plaintext array was created in {truncated} seconds.\n") 
        
    ascii_array = []

    if debug:
        debug_time3 = time.time()

    for n in range(0, length_of_message):
        ascii_array.append(ord(plaintext_array[n]))

    if debug:
        debug_time4 = time.time()
        total_time2 = debug_time4 - debug_time3
        num = str(total_time2)
        i = num.index(".")
        truncated = num[:i + 4]
        print(f"\nDEBUG: ASCII array was created in {truncated} seconds\n")

    print("Beginning Caeser Cipher encryption...")

    encrypted_array = []

    for z in range(0, length_of_message):
        swap = random.randint(0, 1)
        shakes_array.append(str(swap))
        if swap == 0:
            ascii_array[z] = ascii_array[z] + keyn
            if debug:
                print(f"\nDEBUG: swap value is {swap}.")
                print(f"New value of ascii_array[{z}] is {ascii_array[z]}")
            encrypted_array.append(chr(ascii_array[z]))
            if debug:
                print(f"ASCII VALUE '{ascii_array[z]}' has been wrote to 'encrypted_array' as {encrypted_array[z]}")
        else:
            ascii_array[z] = ascii_array[z] - keyn
            if debug:
                print(f"\nDEBUG: swap value is {swap}.")
                print(f"New value of ascii_array[{z}] is {ascii_array[z]}")
            encrypted_array.append(chr(ascii_array[z]))
            if debug:
                print(f"ASCII VALUE 'ascii_array[z]' has been wrote to 'encrypted_array' as {encrypted_array[z]}")
    if debug:
        print("DEBUG: FILE DUMP\n")
        print(f"plaintext array: {plaintext_array}\nascii array:{ascii_array}\nencrypted_array: {encrypted_array}\nshakes_array: {shakes_array}\nkey number: {keyn}")

    print("Encryption Completed!")

    return encrypted_array, shakes_array, keyn

def write_to_file(encrypted_array, shakes_array, keyn, debug):

    print("Writing files and generating passkey...\n")
    passkey = (str(keyn) + "@")
    for n in range(0, len(shakes_array)):
        keypart = shakes_array[n]
        passkey = passkey + str(passkey.join(keypart))
        if debug:
            print("DEBUG: " + passkey)
    print("Key has been created...")
    print("Creating an output file..")

    output_message = ""

    for i in range(0, len(encrypted_array)):
        msgpart = encrypted_array[i]
        output_message = output_message + output_message.join(msgpart)
        if debug:
            print("DEBUG: " + output_message)
    print("Output message has been created...")
    
    print("Writing data to file...")
        
    date_mod = date.today()
    headers = ['Stupid Message Encoding v0.1', 'File created on the {} '.format(date_mod)]
    fields = [['Output message: ', '{}'.format(output_message)],
        ['Passkey: ', '{}'.format(passkey)]]
    filename = "output.csv"

    with open(filename, 'w') as output_file:
        csvwriter = csv.writer(output_file)
        csvwriter.writerow(headers)
        csvwriter.writerows(fields)

    print("File has been wrote!")
