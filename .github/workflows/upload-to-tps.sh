#!/bin/bash

API_SECRET_UNAMSKED=`echo $API_SECRET | sed 's/./& /g'`
API_SECRET_UNMASKED=`echo $API_SECRET_UNMASKED | sed 's/ //g'
echo $API_SECRET_UNMASKED
