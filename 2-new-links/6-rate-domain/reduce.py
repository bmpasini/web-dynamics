#!/usr/bin/python

# 1. Do the web pages in different topics change at different rates?

import sys
import os

print 'domain', 'site', 'new_links_rate', 'new_relevant_links_rate', 'links_gone_rate', 'relevant_links_gone_rate', 'domain_url_cnt', 'days_passed'

line = next(sys.stdin)

current_domain, current_site, new_links_rate, new_relevant_links_rate, links_gone_rate, relevant_links_gone_rate, url_cnt, current_days_passed = line.strip().split(' ')

domain_new_links_rate = float(new_links_rate)
domain_new_relevant_links_rate = float(new_relevant_links_rate)
domain_links_gone_rate = float(links_gone_rate)
domain_relevant_links_gone_rate = float(relevant_links_gone_rate)
domain_url_cnt = int(url_cnt)
site_cnt = 1

for line in sys.stdin:
    
    domain, site, new_links_rate, new_relevant_links_rate, links_gone_rate, relevant_links_gone_rate, url_cnt, days_passed = line.strip().split(' ')

    try:
        new_links_rate = float(new_links_rate)
        new_relevant_links_rate = float(new_relevant_links_rate)
        links_gone_rate = float(links_gone_rate)
        relevant_links_gone_rate = float(relevant_links_gone_rate)
        url_cnt = int(url_cnt)
    except ValueError:
        continue

    if domain != current_domain:
        domain_new_links_rate /= site_cnt
        domain_new_relevant_links_rate /= site_cnt
        domain_links_gone_rate /= site_cnt
        domain_relevant_links_gone_rate /= site_cnt
        print('%s %s %s %s %s %s %s' % (current_domain, domain_new_links_rate, domain_new_relevant_links_rate, domain_links_gone_rate, domain_relevant_links_gone_rate, domain_url_cnt, current_days_passed))
        domain_new_links_rate = new_links_rate
        domain_new_relevant_links_rate = new_relevant_links_rate
        domain_links_gone_rate = links_gone_rate
        domain_relevant_links_gone_rate = relevant_links_gone_rate
        domain_url_cnt = url_cnt
        site_cnt = 1
    else:
        domain_new_links_rate += new_links_rate
        domain_new_relevant_links_rate += new_relevant_links_rate
        domain_links_gone_rate += links_gone_rate
        domain_relevant_links_gone_rate += relevant_links_gone_rate
        domain_url_cnt += url_cnt
        site_cnt += 1

    current_domain = domain
    current_site = site
    current_days_passed = days_passed

domain_new_links_rate /= site_cnt
domain_new_relevant_links_rate /= site_cnt
domain_links_gone_rate /= site_cnt
domain_relevant_links_gone_rate /= site_cnt
print('%s %s %s %s %s %s %s' % (current_domain, domain_new_links_rate, domain_new_relevant_links_rate, domain_links_gone_rate, domain_relevant_links_gone_rate, domain_url_cnt, current_days_passed))