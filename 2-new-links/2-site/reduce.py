#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

print 'domain', 'date', 'site', 'positive', 'negative', 'unknown', 'total', 'new_links', 'new_relevant_links', 'links_gone', 'relevant_links_gone'

line = next(sys.stdin)

current_domain, current_date, current_site, current_url, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

site_positive = int(positive)
site_negative = int(negative)
site_unknown = int(unknown)
site_total = int(total)
site_new_links = int(new_links)
site_new_relevant_links = int(new_relevant_links)
site_links_gone = int(links_gone)
site_relevant_links_gone = int(relevant_links_gone)

for line in sys.stdin:
    
    domain, date, site, url, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

    try:
        positive = int(positive)
        negative = int(negative)
        unknown = int(unknown)
        total = int(total)
        new_links = int(new_links)
        new_relevant_links = int(new_relevant_links)
        links_gone = int(links_gone)
        relevant_links_gone = int(relevant_links_gone)
    except ValueError:
        continue

    if site != current_site or date != current_date:
        print('%s %s %s %s %s %s %s %s %s %s %s' % (current_domain, current_site, current_date, site_positive, site_negative, site_unknown, site_total, site_new_links, site_new_relevant_links, site_links_gone, site_relevant_links_gone))
        site_positive = positive
        site_negative = negative
        site_unknown = unknown
        site_total = total
        site_new_links = new_links
        site_new_relevant_links = new_relevant_links
        site_links_gone = links_gone
        site_relevant_links_gone = relevant_links_gone
    else:
        site_positive += positive
        site_negative += negative
        site_unknown += unknown
        site_total += total
        site_new_links += new_links
        site_new_relevant_links += new_relevant_links
        site_links_gone += links_gone
        site_relevant_links_gone += relevant_links_gone

    if domain != current_domain:
        site_positive = positive
        site_negative = negative
        site_unknown = unknown
        site_total = total
        site_new_links = new_links
        site_new_relevant_links = new_relevant_links
        site_links_gone = links_gone
        site_relevant_links_gone = relevant_links_gone

    current_domain = domain
    current_date = date
    current_site = site
    current_url = url

print('%s %s %s %s %s %s %s %s %s %s %s' % (current_domain, current_site, current_date, site_positive, site_negative, site_unknown, site_total, site_new_links, site_new_relevant_links, site_links_gone, site_relevant_links_gone))

