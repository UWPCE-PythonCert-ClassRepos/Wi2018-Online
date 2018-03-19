#!/usr/bin/env python3
from collections import *


class Donor(dict):

    def __getattr__(self, item):
        if item in self:
            return self[item]
        else:
            raise AttributeError(f'No such attribute: {item} ')

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, item):
        if item in self:
            del self[item]
        else:
            raise AttributeError(f'No such attribute: {item}')

    def append(self, key, value):
        self[key].append(value)


