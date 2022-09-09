import sys
import os
import time


class InfoGathering:

    def __init__(self, domain_name):
        self.domain_name = domain_name

    @staticmethod
    def sleep():
        time.sleep(2)

    def writer(self, command, result):
        with open(command + "_" + self.domain_name + ".txt", "w") as f:
            f.write(result)

    def spawnProc(self, cmd):
        result = os.popen(cmd + self.domain_name).read()
        self.writer(cmd.strip(), result)
        self.sleep()

    def whois(self):
        command = "whois "
        self.spawnProc(command)

    def nslookup(self):
        command = "nslookup "
        self.spawnProc(command)

    def whatweb(self):
        command = "whatweb "
        self.spawnProc(command)

    def dig(self):
        command = "dig "
        self.spawnProc(command)


info = InfoGathering(sys.argv[1])

info.whois()
info.dig()
info.whatweb()
info.nslookup()
