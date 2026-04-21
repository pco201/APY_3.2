"""
    hw4.2.py -- create and sort a dict from access logs with nyuid, bytes pairs.

    Author:  Philippe Ortanez (pco201@nyu.edu)

    Last Revised:  4/16/26
"""

import re

fh = open('access_log.txt')

bytes_count = {}
match_counter = 0

for line in fh:
    match_netid = re.search(r'/~([a-z]{2,3}\d+)', line)
    match_bytes = re.search(r'(\d+)$', line)
    if not match_netid or not match_bytes:
        continue
    nyu_id = match_netid.group(1)
    bytes = int(match_bytes.group(1))
    match_counter = match_counter + 1
    if nyu_id not in bytes_count:
        bytes_count[nyu_id] = 0
    bytes_count[nyu_id] = bytes_count[nyu_id] + bytes

print(f'{match_counter} matches found (both user id and end-of-line bytes found on the line)')
print()

for key in sorted(bytes_count, key=bytes_count.get, reverse=True):
    if bytes_count[key] >= 10000000:
        print(f'{key}:  {bytes_count[key]}')

