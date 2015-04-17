# -*- coding: utf-8 -*-
# Copyright (c) 2014 Spotify AB

from __future__ import absolute_import, division, print_function


#####
# Validation Exceptions
#####


class InvalidRAMLError(Exception):
    pass


class InvalidRootNodeError(InvalidRAMLError):
    pass


class InvalidResourceNodeError(InvalidRAMLError):
    pass


class InvalidParameterError(InvalidRAMLError):
    def __init__(self, message, parameter):
        super(InvalidParameterError, self).__init__(message)
        self.parameter = parameter


#####
# Loader Exceptions
#####

class LoadRAMLFileError(Exception):
    pass
