#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

next(sys.stdin)

for line in sys.stdin:

    domain, site, site_new_links_rate, site_new_relevant_links_rate, site_links_gone_rate, site_relevant_links_gone_rate, site_cnt, days_passed = line.strip().split(' ')

    print('%s %s %s %s %s %s %s %s' % (domain, site, site_new_links_rate, site_new_relevant_links_rate, site_links_gone_rate, site_relevant_links_gone_rate, site_cnt, days_passed))
