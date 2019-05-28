#!/bin/bash

dramatiq geolocation/main.py
 
exec "$@";