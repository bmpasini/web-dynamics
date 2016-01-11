#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

next(sys.stdin)

for line in sys.stdin:

    domain, site, date, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

    print('%s %s %s %s %s %s %s %s %s %s %s' % (domain, date, site, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone))
