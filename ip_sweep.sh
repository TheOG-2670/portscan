#!/bin/bash

#scan all active hosts (0-255) on the local subnet (1) with CIDR of 24
#host 192.168.1.1 is network gateway
#-sn -> don't do a port scan
#-n -> don't do reverse DNS resolution

nmap -sn -n 192.168.1.0/24 | grep -i 192 | cut -d' ' -f5 > ip_list.txt
cat ip_list.txt
