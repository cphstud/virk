#!/bin/bash

wget -O $1.json "http://distribution.virk.dk/offentliggoerelser/_search?q=cvrNummer:$1"
