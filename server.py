import time
from pymavlink import mavutil

# listen for a connection with the given ip
connection = mavutil.mavlink_connection('tcp:localhost:14540')

# send a heartbeat
connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

# send system time every second
while True:
    connection.mav.system_time_send(round(time.time()), 0)
    time.sleep(1)
