import sys


import logging

from usecase.rover_in_plateau_usecase import read_file

#logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if len(sys.argv) < 2:
    print ("txt file not informed")
else:
    print(read_file(sys.argv[1]))