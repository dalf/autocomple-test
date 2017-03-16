#!/bin/bash
cd `dirname $0`
if [ -d "./ve" ]
then
  source ./ve/bin/activate
else
  mkdir -p ve
  virtualenv ve
  source ./ve/bin/activate
  pip install -r requirements.txt
fi
python server.py
