#!/bin/bash 
# "-U Specialisterne - Forensic  - Thorbjoern Wulf - twu@specialisterne.com"
cnt=$2

if [ $(( cnt % 150 )) -gt 0 ]; then
  wget -q -O "$1.json" "-U Specialisterne - Forensic  - Thorbjoern Wulf - twu@specialisterne.com" "https://cvrapi.dk/api?country=dk&vat=$1"
else 
  sleep 10
fi
