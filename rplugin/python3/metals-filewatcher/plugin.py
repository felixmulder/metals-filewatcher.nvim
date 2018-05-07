#!/usr/bin/env python3
import time
import re
import os
import neovim

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

FILE_CREATED  = 1
FILE_MODIFIED = 2
FILE_DELETED  = 3

class Handler(FileSystemEventHandler):
    def __init__(self, pattern, nvim):
        self.nvim = nvim
        self.cwd = os.getcwd()
        self.pattern = re.compile(pattern)
        self.thread = None

    def notify_metals(self, event_type, path):
        path = "file://" + os.path.abspath(path)
        cmd = { "changes": [{ "uri": path, "type": event_type }] }
        self.send_cmd(cmd)

    def send_cmd(self, cmd):
        nvim.call("LanguageClient#Notify", args=["workspace/didChangeWatchedFiles", cmd])

    def is_valid(self, event):
        return not event.is_directory and \
                self.pattern.match(event.src_path) != None

    def on_created(self, event):
        if self.is_valid(event):
            self.notify_metals(FILE_CREATED, event.src_path)

    def on_modified(self, event):
        if self.is_valid(event):
            self.notify_metals(FILE_MODIFIED, event.src_path)

    def on_deleted(self, event):
        if self.is_valid(event):
            self.notify_metals(FILE_DELETED, event.src_path)

@neovim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.path = ".*\.semanticdb"
        self.handler = Handler(self.path, nvim)
        self.observer = Observer()
        self.observer.schedule(self.handler, '.', recursive=True)
        self.nvim = nvim

    @neovim.function('StartMyWatch', sync=True)
    def start_my_watch(self, args):
        self.observer.start()

    @neovim.function('StartMyWatch', sync=True)
    def stop_my_watch(self, args):
        self.observer.stop()
        self.observer.join()
