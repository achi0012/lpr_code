#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will stop LPR Edge"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Stopping LPR Edge..."
if [ -f edge.pid ]
then
  kill -15 `cat edge.pid`
  echo "Stopped LPR Edge"
else
  echo "Could not locate edge.pid - unable to stop LPR Edge"
fi 

        
