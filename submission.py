import pyotp
import time
import sys
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode

base32secret = pyotp.random_base32() # returns a 16 character base32 secret. Compatible with Google Authenticator and other OTP apps
print('Secret: ', base32secret)

totp_uri = pyotp.totp.TOTP(base32secret).provisioning_uri(
    "manjukuah@google.com",
    issuer_name="Secure App")
print(totp_uri)

totp = pyotp.TOTP(base32secret)

code = totp.now()
print("Current OTP: ", code)

# String which represents the QR code 
s = totp_uri
# Generate QR code 
url = pyqrcode.create(s) 
# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 8) 
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
print("Created QR code")
 
# OTP verified for current time
print("Valid Code: ", totp.verify(code)) # => True
print("Waiting 30s")
time.sleep(30)
print("Valid Code: ", totp.verify(code)) # => False