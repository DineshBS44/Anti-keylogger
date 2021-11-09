#!/usr/bin/
from subprocess import Popen, PIPE
import os, signal
from sys import stdout
from re import split
import re


class Process(str):
    ''' Data structure to store the output of 'ps aux' command '''

    user = ""
    pid = ""
    cpu = ""
    mem = ""
    vsz = ""
    rss = ""
    tty = ""
    stat = ""
    start = ""
    time = ""
    cmd = ""

    def _init_(self, proc_info):
        self.user = proc_info[0]
        self.pid = proc_info[1]
        self.cpu = proc_info[2]
        self.mem = proc_info[3]
        self.vsz = proc_info[4]
        self.rss = proc_info[5]
        self.tty = proc_info[6]
        self.stat = proc_info[7]
        self.start = proc_info[8]
        self.time = proc_info[9]
        self.cmd = proc_info[10]
        print(self.cmd)

    def to_str(self):
        return '%s %s %s' % (self.user, self.pid, self.cmd)

    def name(self):
        return '%s' % self.cmd

    def procid(self):
        return '%s' % self.pid


def kill_logger(key_pid):
    stdout.write("\n\nDo you want to stop this process: y/n ?"),
    response = input()
    if (response == "y" or response == "Y"):
        os.kill(int(key_pid), signal.SIGKILL)
    else:
        pass


def get_process_list():
    ''' Retrieves a list of Process objects representing the active process list list '''
    process_list = []
    sub_process = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
    # Discard the first line (ps aux header)
    sub_process.stdout.readline()
    for line in sub_process.stdout:
        # The separator for splitting is 'variable number of spaces'
        print(line)
        # proc_info = line.split()
        line = str(line)
        proc_info = re.findall(r'\S+', line)
        print(proc_info)
        process_list.append(proc_info)
    return process_list


process_list = get_process_list()
stdout.write('Reading Process list...\n')
process_cmd = []
process_pid = []
for process in process_list:
    process_cmd.append('%s' % process[10])
    process_pid.append('%s' % process[1])
l1 = ["logkey", "keylog", "keysniff", "kisni", "lkl", "ttyrpld", "uber", "vlogger"]
record = 0
flag = 1
for x in process_cmd:
    print("x: " + x)
    for y in l1:
        if (x.find(y) > -1):
            stdout.write("KeyLogger Detected: \nThe following proccess may be a keylogger: \n\n\t" + process_pid[
                record] + " - --> " + x)
            kill_logger(process_pid[record])
            flag = 0
    record += 1
if (flag):
    print("No Keylogger Detected")
