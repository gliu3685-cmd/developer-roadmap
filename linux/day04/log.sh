#!/bin/bash

DATE=$(date "+%Y-%m-%d")

if [ -z "$1" ]
then
    echo "请输入学习内容"
    exit 1
fi

echo "$DATE $1" >> study.log

echo "Log saved!"
