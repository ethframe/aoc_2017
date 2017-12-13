import os

import requests
from bs4 import BeautifulSoup

YEAR = 2017
SESSION = ""


def post(day, answer, part_two=False):
    resp = requests.post("https://adventofcode.com/{}/day/{}/answer".format(YEAR, day),
                         data={"level": 2 if part_two else 1,
                               "answer": answer},
                         cookies={"session": SESSION})
    if resp.status_code != 200:
        print("Error {}".format(resp.status_code))
        return
    soup = BeautifulSoup(resp.text, "lxml")
    print(soup.find("article").find("p").text)


def store_input(day):
    target = "day{:02d}.txt".format(day)
    if os.path.exists(target):
        with open(target, "r") as fp:
            return fp.read()
    resp = requests.get("https://adventofcode.com/{}/day/{}/input".format(YEAR, day),
                         cookies={"session": SESSION})
    if resp.status_code != 200:
        print("No input found")
        return None
    with open(target, "w") as fp:
        fp.write(resp.text)
    return resp.text
