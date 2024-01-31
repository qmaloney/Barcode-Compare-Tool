print("")
print("Script that helps you find the Right SN:")
print("")
def find_sn():
    correct_sn = str(input("Please Enter SN you want to find: ")).lower()
    print(correct_sn)

    entered_sn = input("Enter the serial number in your custody: ").lower()

    while entered_sn != correct_sn:
        print("")
        print("The serial number does not match.")
        print("")
        entered_sn = input("Please enter the serial number again: ").lower()
    print("")
    print("YOUR SN MATCHES!")
    print("")

    while True:  # Repeat until correct input is provided
        repeat = input("Do you want to repeat the script? (yes/no): ")
        try:
            if repeat.lower() == "yes":
                find_sn()
            elif repeat.lower() == "no":
                print("Goodbye!")
                while True:
                    pass
                #break  # Exit the loop if 'no' is entered
            else:
                raise ValueError  # Raise an error for any other input
        except ValueError:
            print("Invalid input. Please enter either 'yes' or 'no'.")
    
    
    '''repeat = input("Do you want to repeat the script? (yes/no): ")
    if repeat.lower() == "yes":
        find_sn()'''

find_sn()
