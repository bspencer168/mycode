#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0
linecnt=0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        linecnt+=1
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("line",str(linecnt)+": Failed login by", line.split(" ")[-1].rstrip('\n'))
        elif " GET " in line or " POST " in line:
            loginsuccess+=1

print("The number of failed log in attempts is", loginfail)
print("The number of successful log in attempts is", loginsuccess)