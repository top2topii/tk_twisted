import sys
import subprocess

theproc = subprocess.Popen([sys.executable, "test_klein.py"])
theproc.communicate()

theproc2 = subprocess.Popen([sys.executable, "test_klein2.py"])
theproc2.communicate()