#!/usr/bin/python3

import browser_cookie3 as bc
import requests
import sys
import os


def get_puzzle_input(day: str):
    cookies = bc.chrome()

    url = f"https://adventofcode.com/2024/day/{str(day)}/input"

    try:
        response = requests.get(url, cookies=cookies)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh)
        print(errh.args[0])
    except requests.exceptions.ReadTimeout as errrt:
        print(errrt)
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error. Retrying with alternate port.")
        print(conerr)

    print(response.status_code)
    return response.text

if __name__ == '__main__':

    if len(sys.argv) == 2:
        day = int(sys.argv[1])
        stringform = f'Day0{day}' if day <= 9 else f'Day{day}'
        try:
            os.mkdir(stringform)
        except:
            print("Directory already exists!")
        
        with open(f'./{stringform}/input', 'w') as fd:
            fd.write(get_puzzle_input(day))
        try:
            os.link(f'./aocutils.py', f'./{stringform}/aocutils.py')
        except:
            print("Error making link!")
        try:
            os.link(f'./printed_parsing.py', f'./{stringform}/printed_parsing.py')
        except:
            print("Error making link!")

        os.system(f'cp ./aoc.py ./{stringform}/')
    else:
        print('\nMust give DAY to function\n')
        sys.exit(1)
