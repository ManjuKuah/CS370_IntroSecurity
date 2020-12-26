How to run my python code correctly

Install Python 3.8.3 from python.org

Type 'python' in cmd to check if python is installed correctly. You should see "Python 3.8.3"

If you don't see Python 3.8.3 Make sure your path to python is set correctly. guide: https://projects.raspberrypi.org/en/projects/using-pip-on-windows/4

Update pip by typing 'python -m pip install --upgrade pip' in command prompt

Install pyotp 2.3.0. Type 'pip install pyotp' in cmd

Install pyarcode module. Type 'pip install pyqrcode' and 'pip install pypng' in command prompt

Run submission.py from command prompt

Navigate to submission.py directory
	example:
	code_directory>python submission.py

I do not have Argv arguments so just run submission.py and scan myqr.png with google authenticator during the 30 second wait period. OTP should come out the same as QR Code.



