import pty, os
def process_parent_child():
    (process_id, fd) = pty.fork()
    print("The Process ID for the Current process is: " + str(os.getpid()))
    print("The Process ID for the Child process is: " + str(process_id))
process_parent_child()
master, slave = pty.openpty()

import code
code.interact(local=locals())
# print('Name of the Master: ' + str(os.ttyname(master)))
# print('Name of the Slave: ' + str(os.ttyname(slave)))