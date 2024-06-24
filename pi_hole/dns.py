# this is a simple helper script to setup the dns, i will find and ipliment a permant fix
# either by editing my mechines settings or my routers

import os

if "wifi_names.txt" not in os.listdir(os.path.dirname(os.path.realpath(__file__))):
  print("[!] setting up config [!]")
  file = open("wifi_names.txt", "x+")
  wifi_name = input("please enter your wifi : ")
  dns_name = input("please enter your dns ip (eg: dns1, dns2 : ")
  file.write(wifi_name+"#"+dns_name)
  file.close()
  print("[!] setup done, continuing with script [!]")


data = open("wifi_names.txt", "r")
txt = data.read().split("#")

print("Setting dns")

connectionName=txt[0]
dns1=txt[1]

os.system("nmcli con modify  '"      +connectionName+ "' ipv4.ignore-auto-dns yes")
os.system('nmcli con modify  ' + "'" +connectionName+ "'" + ' ipv4.dns "'+ dns1 + '"')
os.system("nmcli con down    '"      +connectionName+ "'" )
os.system("nmcli con up      '"      +connectionName+ "'" )

print("Done!")
print("to revert the changes simple type 'nmcli dev con modify ipv4.ignore-auto-dns no' and restart your wifi")
