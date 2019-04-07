#!/usr/bin/env python 
import os
import csv
import time 
import sys
import re
import paramiko
import argparse 

# os.system ('pwd')
parser = argparse.ArgumentParser(description='Script to on/off home server')
parser.add_argument('on/off',metavar= '<provide operation>',help = 'start the server via idrac')
args = parser.parse_args()

host = '192.168.0.120'
i = 1

# Try to connect to the host.
# Retry a few times if it fails.
while True:
    print "Connecting to %s (%i/2)" % (host, i)

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,username = "root",password = "calvin")
        time.sleep(3)
        print "Connected to %s" % host
        break
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s" % host
        sys.exit(1)
    except:
        print "Could not SSH to %s, waiting for it to start" % host
        i += 1
        time.sleep(2)

    # If we could not connect within time limit
    if i == 2:
        print "Could not connect to %s. Giving up" % host
        sys.exit(1)


ssh1 = 	ssh.invoke_shell()
print "============Interactive shell starting ============"
time.sleep(0.5)
#print sys.argv[1] ( argv can be on or off)
if sys.argv[1].lower() == "off":
	ssh1.send("racadm serveraction powerdown\n"),time.sleep(3)
	op0 = ssh1.recv(71).strip()
	print op0
elif sys.argv[1].lower() == "on":
	ssh1.send("racadm serveraction powerup\n"),time.sleep(5)
	op1 = ssh1.recv(71).strip()
	print op1
else:
	print "Go away"
# print output
# # Send the command (non-blocking)
# stdin, stdout, stderr = ssh.exec_command("ll")

# # Wait for the command to terminate
# while not stdout.channel.exit_status_ready():
#     # Only print data if there is data to read in the channel
#     if stdout.channel.recv_ready():
#         rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
#         if len(rl) > 0:
#             # Print data from stdout
#             print stdout.channel.recv(1024),

#
# Disconnect from the host
#
ssh.close()