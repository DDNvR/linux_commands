# Command Line Fu
command to help out for when you in the terminal\
--------------------------------------------------------\
**###normal rsync**\
rsync -avzh root@source.com:/pwd/ destination/pwd/file\
\
**###jump via another host that can connect to destination**\
rsync -avzh -e "ssh -J root@source1.com,root@source2.com" root@source.com:/pwd/ destination/pwd/file\
\
**###pivot ssh**\
ssh -t root@source.com ssh root@destination.com\
\
**###short update and upgrade**\
apt update ; apt upgrade\
\
**###change mnt directory to mount drive**\
ls -lsah / | egrep -e "mnt" | awk {'print $2,$6,$10'} | sed -e "s/mnt/mount drive/g" | cut -d "e" -f 1\
\
**###calculator**\
echo $((4 + 2))\
\
**###samba connect**\
smbclient -N -L \\\\YOUR_TARGET_IP\\DIRECTORY_NAME\
smbclient //192.168.0.50/sharedFolderName/ -m SMB3\
\
**###change mac address**\
ifconfig eth0 down \
ifconfig eth0 hw ether 02:5d:6c:e8:8d:b2 \
ifconfig eth0 up \
\
**###check if eth0 mac address has changed**\
tcpdump -i eth0 -e -n "icmp and host 192.168.0.2"\
\
\
**###mac to monitor mode**\
ifconfig eth0 down \
ifconfig eth0 mode monitor \
ifconfig eth0 up \
\
**###generate ssl certificate 2048 bit strong - no CA**\
openssl genrsa -out epp.key 2048\
openssl req -new -x509 -key epp.key -out epp.crt -days 365\
cat epp.key epp.crt > epp.pem\
\
**###show contents of ssl certificate**\
openssl s_client x509 -in name.crt -text -noout\
\
**###connect to server**\
openssl s_client -connect server.com -cert name.crt -key name.key -verify 10 -debug\
\
**###for loop file**\
for i in $(cat list);do echo $i; done\
\
**###random mac address**\
///file NAME: mac.sh
```
#!/bin/bash
LC_CTYPE=C
MAC=00:14:7C #3COM CARD
for i in {1..3}
do
    IFS= read -d '' -r -n 1 char < /dev/urandom
    MAC+=$(printf -- ':%02x\n' "'$char")
done
printf '%s\n' "$MAC"

# ----------------------------------------
# chmod +x mac.sh
# $ ./mac.sh 
# ba:aa:92:cf:38:2e
# use mac/oui address lookup file in git
```
