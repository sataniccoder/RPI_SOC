# Explain
this section i will document the setup of my rpi3   

## Step (1/2) Preparation
I creaded a bootable SD card by downloading this [ISO](https://downloads.raspberrypi.com/raspios_lite_armhf/images/raspios_lite_armhf-2024-03-15/2024-03-15-raspios-bookworm-armhf-lite.img.xz) from the offical RPI website   
After that i added to the **/boot/** section on the SD card a **ssh** file and a **wpa_supplicant.conf** with the following text
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«your_ISO-3166-1_two-letter_country_code»

network={
    ssid="<<SSID>>"
    psk="<<PASSW>>"
    key_mgmt=WPA-PSK
}
```

## Step (2/2) first boot
Once it had booted and connected to my network i ssh'd into the mechine using the default user and password then i ran ```passwd``` and changed it to something new   
now it's time to update and install the software i want here's the command i ran for snort and openvpn
``` bash
pi@raspberrypi:~ $ sudo su
pi@raspberrypi:~ $ apt update && sapt upgrade
pi@raspberrypi:~ $ apt install snort openvpn -y
```

## End
now it's time to setup snort, you can read about it [here](https://github.com/buffkermitisagod/RPI_SOC/snort/readme.md)
