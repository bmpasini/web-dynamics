#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

next(sys.stdin)

for line in sys.stdin:

    domain, site, url, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed = line.strip().split(' ')

    print('%s %s %s %s %s %s %s' % (domain, site, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed))
