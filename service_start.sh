#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will start LPR Service"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Starting LPR Edge..."
nohup python3 -m Service.service_main > service_main.out 2> service_main.err &
serverpid=$!
echo $serverpid >> service_main.pid
echo "Started LPR Service with PID $serverpid"
exit

        
