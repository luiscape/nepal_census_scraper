#!/bin/bash

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install requests[security]