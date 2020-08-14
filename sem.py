import shakelib, shakelib2, csv
debug = False 

print()
print("Stupid Message Encoding -- v0.1")
print("------------------------------------------")


if debug:           #Begin startup checks.
    print("DEBUG MODE ENABLED\n")
    try:
        shakelib.test("Test")
    except:
        print("FATAL ERROR")
        print("DEBUG: module 'shakelib' hasn't loaded correctly.\n")
    else:
        print("DEBUG: module 'shakelib' has loaded correctly.\n")

    try:
        shakelib2.test("Test")
    except:
        print("FATAL ERROR")
        print("DEBUG: module 'shakelib2' hasn't loaded correctly\n")
    else:
        print("DEBUG: module 'shakelib2' has loaded correctly.\n")

#32 to 126
ced = False     #   ced / 'Check Encrypt Decrypt'
                #   Depending on the user input it will use a bool
                #   to use either 'shakelib' or 'shakelib2'
while not ced:

    try:
        ced_input = int(input("Encrypt/Decrypt? (0/1): "))
    except ValueError:
        print("Error :( Please enter either 0 or 1.\n")
    
    try:
     if ced_input > 1 and ced_input < 0: 
         print("Error :( Please enter either 0 or 1.\n")
     else:
         if ced_input == 1:
             ced = True
         else:
            ced = True
    except:
        print("Error :( Please enter either a 0 or a 1\n")
#get message, key number, length of msg

message = ""
key_number = 0

while message == "":
    message = input("Message: ")
while key_number == 0:
    try:
        key_number = int(input("Key Number: "))
    except:
        print("Error :( Please enter a number larger than 0.")
        
print("\nAll required data collected...")
if ced_input == 1:
    print("Beginning encryption!")
    enc_arr, sh_arr, key_number = shakelib.encrypt(message, key_number, debug)
    shakelib.write_to_file(enc_arr, sh_arr, key_number, debug)
else:
    print("Beginning decryption!")
