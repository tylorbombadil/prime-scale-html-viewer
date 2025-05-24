# Diagnostic script to print Python runtime context
import os
import sys

print("Script file location:", __file__)
print("Current working directory:", os.getcwd())
print("Python executable:", sys.executable)
print("Python path root:", sys.path[0])
