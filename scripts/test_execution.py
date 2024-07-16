from geotostitcher.executer import Executer
import time
from datetime import datetime

cmd_file = '/home/rashik/workspace/geoautomation/mrcsource-pave-out/intermediate/pgf2jpg_101.txt'

exe = Executer()
exe.prepare_execution(cmd_file, 1)
input()

exe.start()

d1 = datetime.now()
while(1):
    percent, count, done = exe.get_progress()
    print("-------------------------------------------> Percent and count:", percent, count)
    time.sleep(0.1)
    if done:
        break
d2 = datetime.now()

delta = d2 - d1
seconds = delta.total_seconds()
print(f"Completed execution in {seconds} seconds!")