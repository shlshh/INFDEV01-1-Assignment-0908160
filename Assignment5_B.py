password = raw_input("What is your Password? ")

if len(password) >12:
    print 'Password is Strong'

elif len(password) <6:
    print 'Password is Weak'

else:
    print 'Password is Medium'

if password.isupper():
    print "Your Password only contains capital letters"

if password.islower():
    print "Your Password only contains lower letters"

if password.isdigit():
    print "Your Password only contains numbers"

if '!' in password:
    print ""

elif '@' in password:
    print ""
    
elif '#' in password:
    print ""

elif '$' in password:
    print ""

elif '%' in password:
    print ""

elif '^' in password:
    print ""

elif '&' in password:
    print ""

elif '*' in password:
    print ""

else:
    print "Your Password does not contain a special charactar"