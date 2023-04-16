import getpass
import telnetlib


user = input("Username: ")
password = getpass.getpass()
for ip in range(102,106):
    print("Telnet to Host " + str(ip)) 
    host = "192.168.62." + str(ip)
    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

    tn.write(b"enable\n")
    tn.write(b"123\n")

    tn.write(b"config t \n") 
    for vlans in range (2, 120):
        tn.write(b" vlan " +str(vlans).encode("ascii") + b"\n")
    tn.write(b"end \n")
    tn.write(b"exit \n")
    print(tn.read_all().decode("ascii"))
