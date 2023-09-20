# import pyautogui as pg 

# import time 

# ani=()


# time.sleep(8)

# for i in range(100):
#     pg.write(ani)
   
#     pg.press("Enter")



import socket

def get_ip_from_referral(referral_url):
    domain = referral_url.split('/')[2]
    ip_address = socket.gethostbyname(domain)
    return ip_address

referral_url = "https://example.com/page"
ip_address = get_ip_from_referral(referral_url)
print("IP-адрес:", ip_address)
