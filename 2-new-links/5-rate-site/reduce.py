#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

print 'domain', 'site', 'new_links_rate', 'new_relevant_links_rate', 'links_gone_rate', 'relevant_links_gone_rate', 'site_cnt', 'days_passed'

line = next(sys.stdin)

current_domain, current_site, new_links_rate, new_relevant_links_rate, links_gone_rate, relevant_links_gone_rate, current_days_passed = line.strip().split(' ')

site_new_links_rate = float(new_links_rate)
site_new_relevant_links_rate = float(new_relevant_links_rate)
site_links_gone_rate = float(links_gone_rate)
site_relevant_links_gone_rate = float(relevant_links_gone_rate)
site_cnt = 1

for line in sys.stdin:
    
    domain, site, new_links_rate, new_relevant_links_rate, links_gone_rate, relevant_links_gone_rate, days_passed = line.strip().split(' ')

    try:
        new_links_rate = float(new_links_rate)
        new_relevant_links_rate = float(new_relevant_links_rate)
        links_gone_rate = float(links_gone_rate)
        relevant_links_gone_rate = float(relevant_links_gone_rate)
    except ValueError:
        continue

    if site != current_site or domain != current_domain:
        site_new_links_rate /= site_cnt
        site_new_relevant_links_rate /= site_cnt
        site_links_gone_rate /= site_cnt
        site_relevant_links_gone_rate /= site_cnt
        print('%s %s %s %s %s %s %s %s' % (current_domain, current_site, site_new_links_rate, site_new_relevant_links_rate, site_links_gone_rate, site_relevant_links_gone_rate, site_cnt, current_days_passed))
        site_new_links_rate = new_links_rate
        site_new_relevant_links_rate = new_relevant_links_rate
        site_links_gone_rate = links_gone_rate
        site_relevant_links_gone_rate = relevant_links_gone_rate
        site_cnt = 1
    else:
        site_new_links_rate += new_links_rate
        site_new_relevant_links_rate += new_relevant_links_rate
        site_links_gone_rate += links_gone_rate
        site_relevant_links_gone_rate += relevant_links_gone_rate
        site_cnt += 1

    current_domain = domain
    current_site = site
    current_days_passed = days_passed

site_new_links_rate /= site_cnt
site_new_relevant_links_rate /= site_cnt
site_links_gone_rate /= site_cnt
site_relevant_links_gone_rate /= site_cnt
print('%s %s %s %s %s %s %s %s' % (current_domain, current_site, site_new_links_rate, site_new_relevant_links_rate, site_links_gone_rate, site_relevant_links_gone_rate, site_cnt, current_days_passed))