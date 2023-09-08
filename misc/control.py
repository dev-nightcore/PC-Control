import os
import ctypes

async def reboot():
    os.system('shutdown -r')

async def shutdown():
    os.system('shutdown –s –t 0')

async def logOut():
    ctypes.windll.user32.LockWorkStation()