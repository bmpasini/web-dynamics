#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

print 'domain', 'site', 'url', 'new_links_rate', 'new_relevant_links_rate', 'links_gone_rate', 'relevant_links_gone_rate', 'days_passed'

line = next(sys.stdin)

current_domain, current_site, current_url, current_date, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

url_new_links = float(new_links)
url_new_relevant_links = float(new_relevant_links)
url_links_gone = float(links_gone)
url_relevant_links_gone = float(relevant_links_gone)
days_passed = 1

for line in sys.stdin:
    
    domain, site, url, date, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

    try:
        new_links = float(new_links)
        new_relevant_links = float(new_relevant_links)
        links_gone = float(links_gone)
        relevant_links_gone = float(relevant_links_gone)
    except ValueError:
        continue

    if url != current_url:
        url_new_links_rate = url_new_links / days_passed
        url_new_relevant_links_rate = url_new_relevant_links / days_passed
        url_links_gone_rate = url_links_gone / days_passed
        url_relevant_links_gone_rate = url_relevant_links_gone / days_passed
        print('%s %s %s %s %s %s %s %s' % (current_domain, current_site, current_url, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed))
        url_new_links = new_links
        url_new_relevant_links = new_relevant_links
        url_links_gone = links_gone
        url_relevant_links_gone = relevant_links_gone
        days_passed = 1
    else:
        url_new_links += new_links
        url_new_relevant_links += new_relevant_links
        url_links_gone += links_gone
        url_relevant_links_gone += relevant_links_gone
        days_passed += 1

    if domain != current_domain:
        url_new_links = new_links
        url_new_relevant_links = new_relevant_links
        url_links_gone = links_gone
        url_relevant_links_gone = relevant_links_gone
        days_passed = 1

    current_domain = domain
    current_date = date
    current_site = site
    current_url = url

url_new_links_rate = url_new_links / days_passed
url_new_relevant_links_rate = url_new_relevant_links / days_passed
url_links_gone_rate = url_links_gone / days_passed
url_relevant_links_gone_rate = url_relevant_links_gone / days_passed
print('%s %s %s %s %s %s %s %s' % (current_domain, current_site, current_url, url_new_links_rate, url_new_relevant_links_rate, url_links_gone_rate, url_relevant_links_gone_rate, days_passed))

