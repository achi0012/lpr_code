#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will start LPR Server"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Starting LPR Server..."
nohup uvicorn Server.server_main:app --port=5000 --workers 4 > server_main.out 2> server_main.err &
serverpid=$!
echo $serverpid >> server_main.pid
echo "Started LPR Server with PID $serverpid"
exit

        
