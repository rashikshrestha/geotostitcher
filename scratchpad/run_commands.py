import os
from threading import Thread
import time

# Input parameters
no_of_threads = 100
filename = 'commands.txt'

# Read commands file
f = open(filename, 'r')
lines = f.readlines()
no_of_cmds = len(lines)
print('Total', no_of_cmds, 'commands to execute')

# Thread to execute conversion
class ConversionThread(Thread):
    def __init__(self, commands):
        Thread.__init__(self)
        self.commands = commands
        self.count = 0
 
    def run(self):
        for cmd in self.commands:
            actual_cmd = cmd[:-1]
            os.system(actual_cmd)
            self.count += 1


def get_sublists(lst,n):
    subListLength = len(lst) // n
    list_of_sublists = []
    for i in range(0, len(lst), subListLength):
        list_of_sublists.append(lst[i:i+subListLength])
    return list_of_sublists

sublist = get_sublists(lines, no_of_threads)

thread_list = []

for i in range(no_of_threads):
    thread_list.append(ConversionThread(sublist[i]))

for i in range(no_of_threads):
    thread_list[i].start()

while(1):
    for i in range(no_of_threads):
        print(thread_list[i].count, end=' ')
    print('')
    time.sleep(0.1)