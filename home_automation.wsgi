import os, sys
server_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(server_path)
sys.path.append(server_path)

from server import app as application
