import sys
import shutil
import os
import requests
import argparse
from datetime import date

template_day_default = '03'
template_name_default = 'crossed_wires'

def main(template_day = template_day_default, template_name = template_name_default, copy_computer = False):
    parser = argparse.ArgumentParser(description='An advent of code setup script')
    parser.add_argument("-name")
    parser.add_argument("-day", default = date.today().strftime("%d"))

    args = parser.parse_args()
    name = args.name
    day = args.day

    day_string = 'day-' + day.zfill(2)

    print("Creating day %s with name %s" % (day, name))
    
    shutil.copytree('day-' + template_day, day_string)
    shutil.rmtree(day_string + os.path.sep + '__pycache__')

    os.rename(day_string+os.path.sep+template_name + ".py", day_string + os.path.sep + name + ".py")
    os.rename(day_string + os.path.sep + 'test_' + template_name + ".py", day_string + os.path.sep + 'test_' + name + ".py")

    replace_in_file(day_string + os.path.sep + name + ".py", template_day, day.zfill(2))
    replace_in_file(day_string + os.path.sep + 'test_' + name + ".py", template_name, name)

    if copy_computer:
        shutil.copyfile("computer" + os.path.sep + "ship_computer.py", day_string + os.path.sep + "ship_computer.py")

    input_url='https://adventofcode.com/2019/day/'+str(int(day))+'/input'
    session_id="53616c7465645f5fa025cd768e00b434bf6df6f8043e3905667d29f080f83325842d82af11200dd3a6bf708482188ea0"
    cookies = {"session": session_id}
    headers = {"User-Agent": "advent-of-code-data v0.8.3"}

    response = requests.get(url=input_url, cookies=cookies, headers=headers)
    response.raise_for_status() # ensure we notice bad responses
    file = open(day_string+os.path.sep+"input.txt", "w")
    file.write(response.text.rstrip("\r\n"))
    file.close()

def replace_in_file(filename, replaced, replace):
    # Read in the file
    with open(filename, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(replaced, replace)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

if __name__ == '__main__':
    main()