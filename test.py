
with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","r") as f:
    if str(12345678) in f.read():
        print(True)
    else:
        print(False)


# Add anotther line
with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","r") as fi:
    file = fi.read()
    with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","w") as fil:
        fil.write(file+"987654321\n")

with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","r") as f:
    if str(987654321) in f.read():
        print(True)
    else:
        print(False)

# delete...
with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","r") as f:
    new = f.read().replace("12345678\n","")
    with open("C:\\Users\\jaspe\\Bot\\WelcomeGuilds.txt","w") as fil:
        fil.write(new)

