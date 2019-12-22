#!/usr/bin/env python
# -*- coding: utf-8 -*-

def prError(text): print("\u001b[31;1m{}\033[00m" .format(text))
def prSuccess(text): print("\u001b[32;1m{}\033[00m" .format(text))
def prWorking(text): print("\033[33m{}\033[00m" .format(text))
def prWarning(text): print("\033[93m{}\033[00m" .format(text))
def prChanged(text): print("\u001b[35m{}\033[00m" .format(text))
def prRemoved(text): print("\033[31m{}\033[00m" .format(text))
def prAdded(text): print("\033[94m{}\033[00m" .format(text))
