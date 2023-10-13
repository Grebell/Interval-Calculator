from assign import assignint
from assign import assignmma
a = 20
b = 20
loop = 1
while loop < 2:
    print("Please input the base note (Eb, A#, C, etc...)")
    x = input("> ")
    a = (assignmma(x))
    if a == 20:
        print("Bad input")
    else:
        print("Please input the second note (Db, E#, F, etc...)")
        x = input("> ")
        b = (assignmma(x))
        if b == 20:
            print("Bad Input")
        else:
            a = int(a)
            b = int(b)
            z = 0
            while a != b:
                if a > 12:
                    a = 1
                else:
                    a = a + 1
                    z = z + 1
            if a > 12:
                a = 1
                z = z + 1
            s = (assignint(z))
            if s == 20:
                print("Error")
            else:
                print(s)
    print("Run Again?")
    print("1 for yes")
    print("2 for no")
    loop = int(input("> "))
print("Goodbye")
