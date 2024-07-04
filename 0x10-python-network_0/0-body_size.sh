#!/bin/bash
# Takes in a URL and displays the size of the body of the response
curl -sI "$1" |echo " $headers" grep "Content-Length:"| cut -d":" -f2
