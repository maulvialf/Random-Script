from time import *
from adb_shell.adb_device import AdbDeviceTcp
import adb_shell.constants as constants 
from adb_shell.adb_message import *

device1 = AdbDeviceTcp('adbaby.sstf.site', 6666, default_transport_timeout_s=9.)
device1.connect()
# response1 = device1._service(b"flag", "0002D3d283".encode('utf8'), None, 4, decode=True)
# response1 = device1._service(b"flag", "".encode('utf8'), None, 4, decode=True)
adb_info = device1._open(b"flag:", 1, 1, 1)
# device1.list('.')
sleep(0.2)
msg = AdbMessage(constants.WRTE, adb_info.local_id, adb_info.remote_id, b"0002D3d283\n")
device1._io_manager.send(msg, adb_info)
sleep(0.2)
response1 =device1._io_manager.read([constants.OKAY], adb_info)

# device1._okay(adb_info)
# AdbMessage('WRTE', adb_info.local_id, adb_info.remote_id, filesync_info.send_buffer[:filesync_info.send_idx])
print(response1)
