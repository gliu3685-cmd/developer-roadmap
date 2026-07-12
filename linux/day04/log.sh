#!/bin/bash

DATE=$(date "+%Y-%m-%d")

CONTENT=$1

echo "$DATE $CONTENT" >> study.log

echo "Log saved!"
