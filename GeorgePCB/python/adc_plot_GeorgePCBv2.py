'''
plot adc data
'''

import numpy as np  # To define array and some basic math on arrays
import matplotlib.pyplot as plt  # To plot the data
from subprocess import Popen, PIPE
from time import sleep
import pydevd

# settings
en_remote_dbg = 0  # enable remote debugging. Enable debug server first!
channel_read = 7  # select channel, from 1 to 7

# remote debug setup
server_ip = '192.168.100.5'
client_ip = '192.168.100.2'
if en_remote_dbg:
    from pydevd_file_utils import setup_client_server_paths
    server_path = '/root/ultrasound_python/'
    client_path = 'V:\\ultrasound_python\\'  # client path with samba
    PATH_TRANSLATION = [(client_path, server_path)]
    setup_client_server_paths(PATH_TRANSLATION)
    pydevd.settrace(client_ip)

plt.figure(1)
fig = plt.gcf()
fig.show()

while True:

    process = Popen(['../c_exec/ultrasound_2019_pcb_v2 100 20'],
                    stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = process.communicate()
    stdchar = stdout.split()
    sleep(0.1)
    I = np.genfromtxt('./databank.txt', delimiter=',', dtype=int)

    fig.clf()
    plt.plot(I[channel_read, :])
    fig.canvas.draw()
