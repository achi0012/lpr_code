#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will stop LPR Service"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Stopping LPR Service..."
if [ -f service_main.pid ]
then
  kill -15 `cat service_main.pid`
  echo "Stopped LPR Service"
else
  echo "Could not locate service_main.pid - unable to stop LPR Service"
fi 

        
