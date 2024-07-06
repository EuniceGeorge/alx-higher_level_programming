#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]

    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    payload = {"q": q}
    res = requests.post(url, data=payload)
    try:
        r_dic = res.jason()
        if r_dic:
            print("[{}] {}".format(res.dic.get('id'), res.dic.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
