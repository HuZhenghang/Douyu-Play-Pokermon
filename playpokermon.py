import win32api
import win32con
from danmu import DanMuClient
import time
import datetime

dmc = DanMuClient('http://www.douyu.com/3819143')
if not dmc.isValid(): print('Url not valid')


start = datetime.datetime.now()

command = {
	"left": 0x41,
	"up": 0x57,
	"right": 0x44,
	"down": 0x53,
	"start": 0x0D,
	"k": 0x4B
}

@dmc.danmu
def danmu_fn(msg):
	global start
	button = msg['Content']
	if button=='up' or button=='down' or button=='left' or button=='right' or button=='start' or button=='k':
		end = datetime.datetime.now()
		if (end-start).seconds>1: #read every one second
			win32api.keybd_event( command[button],0,0,0)
			time.sleep(0.1)
			win32api.keybd_event( command[button],0,win32con.KEYEVENTF_KEYUP,0)
			start=end

dmc.start(blockThread = True)


