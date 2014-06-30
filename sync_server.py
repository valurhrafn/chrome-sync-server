""" This is a python sync server used to sync with Chromium """

from third_party.chromium import sync_testserver
import sys

class SyncServer(sync_testserver.SyncServerRunner):
  """The sync server"""

  def __init__(self):
    super(SyncServer, self).__init__()

  def run_server(self):
    sync_testserver.SyncServerRunner.run_server(self)


if __name__ == '__main__':
  sys.exit(SyncServer().main())
