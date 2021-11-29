Vpnumld = False ##phone number does not meet conditions.
while not Vpnumld:
        pnum = input("what is your phone number?")##user inputs a phone number
        npnum = pnum.replace(" " and "-","")##removes all spaces and dashes
        if len(npnum)==10 or len(npnum)==11 or len(npnum)==12 and npnum.isdigit() and npnum[0]!=0:
            Vpnumld = True ##phone number meets condtions. this section formats the number correctly
            numl = len(npnum)
            area = slice(0,5,1) ##formats area code
            line = slice(5,numl,1) ##formats line code
            FullNum= npnum[area]+"-"+npnum[line] ##combines the formatted versions
            print(FullNum) ##prints and stores valid and correctly formatted phone number
        elif npnum == ("help"):
            print("Please make sure your phone number matches the following conditions: \n The phone number is between 10 and 12 digits long \n The phone number has no special characters, only numbers. \n The first digit is a '0'.")
            continue
        else:
            print("Your phone number is invalid! Type 'help' for assistance.")

