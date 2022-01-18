#!/bin/sh
clear
echo "--------------------------------------------------------------------"
echo "This script will start LPR Edge"
echo "Hit return to continue"
echo "Hit Ctrl-C to end this script now!"
echo "--------------------------------------------------------------------"
read DUMMY
echo "Starting LPR Edge..."
nohup python3 -m Edge.edge_main > edge.out 2> edge.err &
serverpid=$!
echo $serverpid >> edge.pid
echo "Started LPR Edge with PID $serverpid"
exit

        
