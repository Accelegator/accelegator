import os
import sys

# set the system path to contain the previous directory
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')
