#!/bin/sh

# wait for Redis server to start
echo "Waiting for redis server"
./wait_for.sh $REDIS_HOST:$REDIS_PORT
celery -A fbCrawler worker -l INFO