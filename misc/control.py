import os

async def reboot():
    os.system('shutdown -r')

async def shutdown():
    os.system('shutdown –s –t 0')