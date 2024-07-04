#!/bin/bash
# Takes in a URL and displays the size of the body of the response
curl -s"$i" | grep  "Content-Length:" 
