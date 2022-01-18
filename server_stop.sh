#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will stop LPR Server"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Stopping LPR Server..."
if [ -f server_main.pid ]
then
  kill -9 `cat server_main.pid`
  echo "Stopped LPR Server"
else
  echo "Could not locate server_main.pid - unable to stop LPR Server"
fi 

        
