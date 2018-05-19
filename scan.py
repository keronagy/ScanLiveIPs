import platform
from Tools.scripts.treesync import raw_input
from netaddr import *
import subprocess
from termcolor import colored
import sys

workingips = set([])

while (1):

    ipAdrress = raw_input('Enter the ip Address range or n to exit:')
    if ipAdrress[0].lower() == "n":
        sys.exit("good bye :D")
    try:
        print()
        ips = list(IPNetwork(ipAdrress))

        for i in range(len(ips)):
            print(colored("Pinging %s" % ips[i], 'blue'))
            if platform.system() == "Windows":
                command = ("ping " + str(ips[i]) + " -n 3 -w " + str(1 * 50))
            else:
                command = "ping -i " + str(1) + " -c 3 " + str(ips[i])
            p = subprocess.Popen(command, stdout=subprocess.PIPE)
            p.wait()
            if p.poll():
                print(colored("%s is down" % ips[i], 'red'))
            else:
                print(colored("%s is up" % ips[i], 'green'))
                workingips.add(ips[i])
            print()
        print(colored("working IPs", 'blue'))
        for i in workingips:
            print(colored(i, 'green'))
        print()
    except:
        print(colored("please enter correct ip address or type n to exit", 'red'))
