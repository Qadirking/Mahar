import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Qadir import knock_Out
    knock_Out()
elif bit == '32bit':
    from Qdr import knock_Out
    knock_Out()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.sys.exit()
