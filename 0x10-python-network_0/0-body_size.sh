#!/bin/env bash
# Displays the size of the body of the response


curl -is $1 | grep -s Content-Length | awk '{print $2}'
