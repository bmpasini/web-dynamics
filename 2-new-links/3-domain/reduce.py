#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

print 'domain', 'date', 'positive', 'negative', 'unknown', 'total', 'new_links', 'new_relevant_links', 'links_gone', 'relevant_links_gone'

line = next(sys.stdin)

current_domain, current_date, current_site, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

domain_positive = int(positive)
domain_negative = int(negative)
domain_unknown = int(unknown)
domain_total = int(total)
domain_new_links = int(new_links)
domain_new_relevant_links = int(new_relevant_links)
domain_links_gone = int(links_gone)
domain_relevant_links_gone = int(relevant_links_gone)

for line in sys.stdin:
    
    domain, date, site, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = line.strip().split(' ')

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

    if domain != current_domain or date != current_date:
        print('%s %s %s %s %s %s %s %s %s %s' % (current_domain, current_date, domain_positive, domain_negative, domain_unknown, domain_total, domain_new_links, domain_new_relevant_links, domain_links_gone, domain_relevant_links_gone))
        domain_positive = positive
        domain_negative = negative
        domain_unknown = unknown
        domain_total = total
        domain_new_links = new_links
        domain_new_relevant_links = new_relevant_links
        domain_links_gone = links_gone
        domain_relevant_links_gone = relevant_links_gone
    else:
        domain_positive += positive
        domain_negative += negative
        domain_unknown += unknown
        domain_total += total
        domain_new_links += new_links
        domain_new_relevant_links += new_relevant_links
        domain_links_gone += links_gone
        domain_relevant_links_gone += relevant_links_gone

    current_domain = domain
    current_date = date
    current_site = site

print('%s %s %s %s %s %s %s %s %s %s' % (current_domain, current_date, domain_positive, domain_negative, domain_unknown, domain_total, domain_new_links, domain_new_relevant_links, domain_links_gone, domain_relevant_links_gone))
