#!/bin/bash

threshold=700
while true; do
  available=$(free -m | head -2 | tail -1 | awk '{print $7}')
  if [ "$threshold" -ge "$available" ]; then
    pkill -f '.*GradleDaemon.*'
  fi
  sleep 10
done
