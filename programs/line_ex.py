with open("programs/lines.txt") as file:
    line_number = 1
    for line in file:
        print("%s %s" % (line_number, line.rstrip()))
