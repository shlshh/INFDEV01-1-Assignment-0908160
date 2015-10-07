tekst = raw_input ("Type Text ")
nummer = int(raw_input ("Type Number "))

count = 0
test = ""

while count <len(tekst):
    i = tekst[count]
    ascii = ord(i)+nummer

    if i.isupper():
        if (ascii > 90):
            ascii = ascii - 26 

        elif (ascii < 65):
            ascii = ascii + 26 

    elif i.islower():
        if (ascii > 122):
            ascii = ascii - 26 

        elif (ascii < 96):
            ascii = ascii + 26

    else:
        ascii = ord(i)

    test += chr(ascii)
    count += 1  
 
print test
