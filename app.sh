#!/bin/bash
# app.sh
clear
echo "Chart Maker" | figlet
echo -e 'by mdeboute' | figlet -f small -c
echo
echo
cd ../chartMaker/src
python3 user_spider_chart.py
