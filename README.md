# FLASK-EIKON
Refinitiv Eikon with flask on window

Prerequisite
------------
1. pip install -r requirement.txt
  * Some of package might be upgrade.
2. Enforce **FLASKEIKON** absolute path on window( w/ advanced setting )
```
FLASKEIKON = /path/of/FLASK-EIKON
```

Configuration
-------------
* resource/config
  * Setup 4 required information
  * ip, port, log path, eikon app id
* resource/flask-eikon.bat
  * Daemonize flask app. You should edit
    * absolute path of python
    * absolute path of launch script location

Usage
-----
* Internally test?: python app/start.py
* Daemonize?: Click resource/flask-eikon.bat

Test Eikon
----------
python timeseries.py
