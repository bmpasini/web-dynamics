#!/usr/bin/python

# 2. Is the rate of new pages arrival different for different topics?

import sys
import os

def links_data(past_day_outlinks, outlinks):

    new_links = 0
    new_relevant_links = 0
    links_gone = 0
    relevant_links_gone = 0

    positive = 0
    negative = 0
    unknown = 0

    for outlink_url, outlink_relevant in outlinks.items():

        if outlink_url not in past_day_outlinks:
            new_links += 1
            if outlink_relevant == '1':
                new_relevant_links += 1
        elif past_day_outlinks[outlink_url] != '1' and outlink_relevant == '1': # in case that outlink becomes relevant
            new_relevant_links += 1

        if outlink_relevant == '1':
            positive += 1
        elif outlink_relevant == '0':
            negative += 1
        else:
            unknown += 1

    total = positive + negative + unknown

    for past_day_outlink_url, past_day_outlink_relevant in past_day_outlinks.items():

        if past_day_outlink_url not in outlinks:
            links_gone += 1
            if past_day_outlink_relevant == '1':
                relevant_links_gone += 1
        elif past_day_outlink_relevant == '1' and outlinks[past_day_outlink_url] != '1': # in case that outlink becomes irrelevant
            relevant_links_gone += 1

    return positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone


print 'crawl_domain', 'url_domain', 'original_url', 'crawl_date', 'positive', 'negative', 'unknown', 'total', 'new_links', 'new_relevant_links', 'links_gone', 'relevant_links_gone'

line = next(sys.stdin)

current_domain, current_site, current_url, current_date, outlink_url, outlink_relevant = line.strip().split(' ')

outlinks = dict()
outlinks[outlink_url] = outlink_relevant

past_day_outlinks = None

for line in sys.stdin:
    
    domain, site, url, date, outlink_url, outlink_relevant = line.strip().split(' ')

    if current_date != date:
        if past_day_outlinks is not None:
            positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = links_data(past_day_outlinks, outlinks)
            print('%s %s %s %s %s %s %s %s %s %s %s %s' % (current_domain, current_site, current_url, current_date, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone))
        past_day_outlinks = outlinks
        outlinks = dict()

    if current_url != url or current_domain != domain:
        past_day_outlinks = None
        outlinks = dict()
    
    outlinks[outlink_url] = outlink_relevant

    current_domain = domain
    current_site = site
    current_url = url
    current_date = date

if past_day_outlinks is not None:
    positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone = links_data(past_day_outlinks, outlinks)
    print('%s %s %s %s %s %s %s %s %s %s %s %s' % (current_domain, current_site, current_url, current_date, positive, negative, unknown, total, new_links, new_relevant_links, links_gone, relevant_links_gone))








