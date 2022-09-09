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

    def whois(self):
        command = "whois "
        result = os.popen(command + self.domain_name).read()
        self.writer(command.strip(), result)
        self.sleep()

    def nslookup(self):
        command = "nslookup "
        result = os.popen(command + self.domain_name).read()
        self.writer(command.strip(), result)
        self.sleep()

    def whatweb(self):
        command = "whatweb "
        result = os.popen(command + self.domain_name).read()
        self.writer(command.strip(), result)
        self.sleep()

    def dig(self):
        command = "dig "
        result = os.popen(command + self.domain_name + "ANY + nostat +nocmd +nocomments").read()
        self.writer(command.strip(), result)
        self.sleep()


info = InfoGathering(sys.argv[1])

info.whois()
info.dig()
info.whatweb()
info.nslookup()
