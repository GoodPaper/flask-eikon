@echo off
ABSOLUTE_PATH\OF\python.exe ABSOLUTE_PATH\OF\FLASK-EIKON\ops\flask-eikon.py stop %*
ABSOLUTE_PATH\OF\python.exe ABSOLUTE_PATH\OF\FLASK-EIKON\ops\flask-eikon.py start %*
pause