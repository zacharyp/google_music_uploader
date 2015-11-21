#!/usr/bin/env python
import argparse
from os import walk, path

from gmusicapi import Musicmanager


def get_file_paths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    for root, directories, files in walk(directory):
        file_gen = (f for f in files if not f.startswith("."))
        for filename in file_gen:
            # Join the two strings in order to form the full filepath.
            filepath = path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def uploadfiles(api, files):
    for f in files:
        upload = api.upload(f, transcode_quality="320k", enable_matching=True)
        print(upload)


def get_dir():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-dir', action='store', dest='dir', required=True,
        help='Full directory path from which to upload songs')
    args = parser.parse_args()
    return args.dir

if __name__ == "__main__":
    directory = get_dir()

    client = Musicmanager()
    logged_in = client.login()

    if logged_in:
        print "Successfully logged in. \n" \
              "Attempting upload songs in directory {}".format(directory)
        uploadfiles(client, get_file_paths(directory))
