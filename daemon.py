#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""
from anki_vector.util import degrees, distance_mm, speed_mmps
import anki_vector  # Robot stuff
import time         # sleep
import os           # os directory level handling
import signal       # To trap ctrl-c
import sys          # To exit

def main():
    # Capture ctrl-c
    signal.signal(signal.SIGINT, signal_handler)

    script_directory = "./vector_scripts_to_run"
    # Lets try to make a directory if it doesn't exist:
    try:
        if not os.path.exists(script_directory):
            os.makedirs(script_directory)

    except:
        print("Looks like I had trouble creating ./vector_scripts_to_run directory.")

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.say_text("I am now in patient SDK mode.", duration_scalar=0.8)

        while 1:
            list_of_files = os.listdir(script_directory)

            for file_name in list_of_files:
                print ("I am running script: " + script_directory + "/" + file_name)
                
                script_to_run_object = open(script_directory + "/" + file_name, "r")

                try:
                    exec(script_to_run_object.read())

                except Exception as e:
                    print ("Your plugin script crashed.  Fix and try again.\n")
                    print (str(e) + "\n")
                    robot.say_text("Your plugin script crashed, fix and try again, see console for details.", duration_scalar=0.6)

                script_to_run_object.close()

                try:
                    os.remove(script_directory + "/" + file_name)
                    print ("file_name: " + file_name + " removed\n")

                except:
                    print ("I had trouble removing the file?")

            time.sleep(1)

def signal_handler(sig, frame):
    print ("Ctrl-c caught")
    sys.exit(0)

if __name__ == "__main__":
    main()
