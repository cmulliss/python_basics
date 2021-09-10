import os

print(os.getcwd())

hosts = open("/etc/hosts")
hosts_contents = hosts.read()
print(hosts_contents + "\n")

# read to get whole file contents

print("Current position: %s" % (hosts.tell()))
print(hosts.read())

hosts.seek(0)
print("Current position after seek: %s" % (hosts.tell()))
print(hosts.read())
hosts.close()
