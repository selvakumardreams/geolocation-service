#!/bin/sh

dramatiq geolocation/main.py
 
exec "$@";