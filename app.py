# Python3 program to print india map pattern
# code by ironsubhajit

a = 0
b = 0
c = 10

s = ("TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs"
     " UJq TNn*RPn/QPbEWS_JSWQAIJO^NBELPe"
     "HBFHT}TnALVlBLOFAkHFOuFETpHCStHAUFA"
     "gcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm S"
     "On TNn ULo0ULo#ULo-WHq!WFs XDt!")

# Read each character of encoded string
a = ord(s[b])

while a != 0:
    if b < 170:
        a = ord(s[b])
        b += 1

        while a > 64:
            a -= 1
            c += 1

            if c == 90:
                c = 10
                print(end=chr(c)) # 10 = \n
            else:
                if b % 2 == 0:
                    print(chr(33), end='') # 33 = ! and 32 = ' '
                else:
                    print(chr(32), end='')
    else:
        break
