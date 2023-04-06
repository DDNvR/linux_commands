# Linux_Commands
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
**###for loop file**\
for i in $(cat list);do echo $i; done\
\
\
**###random mac address**\
///file NAME: mac.sh\
```
#!/bin/bash
LC_CTYPE=C
MAC=00-60-2F
for i in {1..3}
do
    IFS= read -d '' -r -n 1 char < /dev/urandom
    MAC+=$(printf -- '-%02x\n' "'$char")
done
printf '%s\n' "$MAC"
```
