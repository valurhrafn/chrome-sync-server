chrome-sync-server
==================

Sync server for use with Chromium
Most of this code and libraries is from the Chromium source code, wich has a C++ testserver that needs to be compiled.

## To use the server:

Prerequisites:
  * Python 2.7

Example for running the server on port 8090:
  ```python
  python sync_testserver.py --port=8090
  ```
  
there are a few cl options to know about. All other flags are for tasks to use if needed.

- `--port` Port used by the server. If none is specified, the server will listen on an ephemeral port.
- `--host` will set the host to connect to, defaults to 127.0.0.1
- `--log-to-console` Enables sys.stdout logging default is False
- `--log-file` The name of the server log file.
- `--xmpp-port` Port used by the XMPP server. If unpecified, the XMPP server will listen on an ephemeral port.
	

## Chromium settings

Chromium needs to run with command line flags that sets the sync server custom url and enables logging

Linux:
```
chromium-browser --enable-logging --enable-synced-notifications \ --sync-url=http://127.0.0.1:1337/chromiumsync
```

Windows:
```
chrome.exe google-chrome --enable-logging --enable-synced-notifications \ --sync-url=http://127.0.0.1:1337/chromiumsync
```
## Resources

  - [python.org](http://python.org/)
  - [chromium](http://chromium.org/)

## TODO

  - Run as production server
  - Save logged data

  
## License
[MIT licence](http://opensource.org/licenses/MIT)
