# -*- coding: utf-8 -*-


class BackgroundTaskError(Exception):

    def __init__(self, message, errors=None):
        super(BackgroundTaskError, self).__init__(message)
        self.errors = errors
