# Explain
this section will cover how i setup snort as a simple IDS, the porpuse of this is too check my networks traffic and alart me of anything i might want to investigate

## Step (1/x) Setup
if you read the setup part, then snort should be installed if it's not use ```sudo apt install snort -y``` to install it on your RPI   

setting up the config, this is a test one so it's not going to do anything special but you can use the [free rules](https://www.snort.org/downloads/community/snort3-community-rules.tar.gz) if you wish   
this will be done in the home dir and the layout is this
```
╔═Home_dir/
╠═════config/
╠═══════snort.rules
╠═════logs/
╚═══════snort/
```

## Step (2/x) Rules
to test it i made a simple rule that would alert me of an ssh connections
```
# test rules file
alert tcp any any -> any 22 (msg:"Potential SSH Connection"; sid:10000002; rev:1;)
```
to run snort i used the command
```
pi@raspberrypi:~ $ snort -c config/snort.rules -l logs/snort
```
then going back to our mechine we can ssh into it using ```ssh pi@<ip>```, going back to our log file we can see it's given us an alert

```
log file at ~/logs/snort/alert
command cat ~/logs/snort/alert

[**] [1:10000002:1] Potential SSH Connection [**]
[Priority: 0] 
06/20-19:06:01.599853 <my_up>:<port> -> <rpi_ip>:22
TCP TTL:64 TOS:0x0 ID:0000 IpLen:20 DgmLen:00 DF
******S* Seq: 0x00000000  Ack: 0x0  Win: 0x0000  TcpLen: 40

```

## afterword
i haven't fully made my own snort config, but when the rest of the project it done i will be returing too it to add more rules to check for things on the openvpn etc...   
the next step is setting up my openvpn server and port forwading it so i can securly connect to it outside of my LAN
