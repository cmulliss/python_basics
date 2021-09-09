from os import closerange


print("Started reading the file.")
with open("/etc/hosts") as hosts:
    print("File closed? %s" % (hosts.closed))
    print(hosts.read())
    print(hosts.mode)
print("Finished reading the file.")
print("File closed? %s" % (hosts.closed))

# file will stay open while in 'with open' block
print("\n\n")

with open("programs/lines.txt") as the_file:

    for line in the_file:
        print(line.rstrip())


# rstrip to strip newline chars

print("\n\n")
