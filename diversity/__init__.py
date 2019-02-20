#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# check that python version is at least 3.6
if sys.version_info.major < 3 or sys.version_info.minor < 6:
    raise Exception("Python 3.6 or a more recent version is required.")

from .greedy import greedy
from .neighborhood import neighborhood
from .interchange import interchange
