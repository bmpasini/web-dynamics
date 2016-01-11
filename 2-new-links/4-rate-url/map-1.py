#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

next(sys.stdin)

for line in sys.stdin:

    domain, site, url, date, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')
    
    print('%s %s %s %s %s %s %s %s' % (domain, site, url, date, new_links, new_relevant_links, links_gone, relevant_links_gone))
