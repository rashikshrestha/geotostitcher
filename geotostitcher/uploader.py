import os
import sys

if __name__=='__main__':
    print("Uploading...")
    
    #! Get commands
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        commands = [line[:-1] for line in f]
    commands.sort()
    
    #! Run commands
    for c in commands:
        print("\n\n---------------------------------------")
        print("EXECUTING:", c)
        print("Please wait...")
        os.system(c)
        print("---------------------------------------")