#!/usr/bin/env python
from gmusicapi import Mobileclient
from gmusicapi import Musicmanager
from getpass import getpass

api = Musicmanager()

api.perform_oauth()
