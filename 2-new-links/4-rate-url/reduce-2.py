#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys

print 'domain', 'site', 'url', 'new_links_rate', 'new_relevant_links_rate', 'links_gone_rate', 'relevant_links_gone_rate', 'days_passed'

current_url = None
url = None

for line in sys.stdin:

    line = line.strip().split(' ')

    if len(line) == 1:

        current_url = line[0]

    elif len(line) == 8:

        url, domain, site, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed = line

    if current_url == url:

        print('%s %s %s %s %s %s %s %s' % (domain, site, url, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed))
