#!/usr/bin/env python

import os
import re

def find_file_by_pattern(pattern='.*', base=".", circle=True):
    re_file = re.compile(pattern)
    if base == '.':
        base = os.getcwd()

    final_file_list = []
    cur_list = os.listdir(base)

    for item in cur_list:
        full_path = os.path.join(base, item)

        if os.path.isfile(full_path):
            if re_file.search(full_path):
                final_file_list.append(full_path)

        else:
            final_file_list += find_file_by_pattern(pattern, full_path)

    return final_file_list



