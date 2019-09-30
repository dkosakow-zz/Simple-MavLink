import time
from pymavlink import mavutil

# initiate a connection with the specified ip
connection = mavutil.mavlink_connection('tcpin:localhost:14540')
connection.wait_heartbeat()

while True:
    time.sleep(1)
    # read in next message
    msg = connection.recv_msg()

    # if no message we assume that the server disconnected
    if msg is None:
        print("connection lost")
        break
    else:
        print(msg.time_unix_usec)
