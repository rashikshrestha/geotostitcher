import os
from threading import Thread

class ConversionThread(Thread):
    """
    Thread class to run threads
    """
    def __init__(self, commands):
        Thread.__init__(self)
        self.commands = commands
        self.count = 0
        self.done = False
 
    def run(self):
        for cmd in self.commands:
            #! Execute a command
            os.system(cmd)
            #! Increase the counter after execution is completed
            self.count += 1
        self.done = True


class Executer():
    """
    Execute the commands in parllel

    Attributes
    ----------
    filepath: str
        Path to files with commands to run
    no_of_threads: int
        Number of parallel processes to run
    
    """
    def __init__(self, filepath, no_of_threads) -> None:

        #! Get commands and group it
        commands = self.get_commands(filepath)
        commands_groups = self.get_sublists(commands, no_of_threads)
        self.total_threads = len(commands_groups)

        #! Create threads
        self.thread_list = []
        for i in range(self.total_threads):
            self.thread_list.append(ConversionThread(commands_groups[i]))


    def start(self):
        """
        Start execution of commands
        """ 
        for i in range(self.total_threads):
            self.thread_list[i].start()


    def get_progress(self):
        """
        Get the progress on the commands
        """
        total_count = 0
        done = False
        for i in range(self.total_threads):
            total_count += self.thread_list[i].count

            if i==0:
                done = self.thread_list[i].done
            else:
                done = done and self.thread_list[i].done

        return total_count, done 


    def get_commands(self, file_path):
        """
        Get commands list from the file
        """
        with open(file_path, 'r') as f:
            commands = [line[:-1] for line in f]
    
        return commands


    def get_sublists(self, lst, n):
        """
        Divide the entire list of commands to number of threads
        """
        subListLength = len(lst) // n
        list_of_sublists = []
        for i in range(0, len(lst), subListLength):
            list_of_sublists.append(lst[i:i+subListLength])
        return list_of_sublists