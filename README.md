# geolocation-service

## Overview
An asynchronous geolocation service to perform geocoding of addresses and reverse-geocoding of long/lat coordinates.

## Why Dramatiq library
#TODO

## Broker - RabbitMQ
#TODO

## Backend - Redis
#TODO

## Geocoder
#TODO

# Installation

1. Install RabbitMQ and Redis

2. Geocoder
```bash
$ pip install geocoder
```
3. Dramatiq with RabbitMQ
```bash
$ pip install dramatiq[rabbitmq]
```
4. Dramatiq with Redis
```bash
$ pip install dramatiq[redis]
```
5. Watch
```bash
$ pip install watchdog_gevent
$ pip install watchdog
```

# Running the application
1. Run RabbitMQ: rabbitmq-server
2. Run Redis: redis-server
3. Run a batch file workers.bat
4. In another terminal, run python main.py "H. C. Andersens Blvd. 27, 1553 København V, Denmark"
5. In another terminal, run python main.py "(55.674146, 12.569553)"
