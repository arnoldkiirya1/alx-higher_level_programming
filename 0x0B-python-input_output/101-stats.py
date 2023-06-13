#!/usr/bin/python3

import sys

def print_stats(file_size, status_codes):
    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))

def parse_line(line):
    try:
        line_parts = line.split()
        file_size = int(line_parts[-1])
        status_code = int(line_parts[-2])
        return file_size, status_code
    except:
        return None, None

def compute_metrics():
    count = 0
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size and status_code:
                count += 1
                file_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

                if count % 10 == 0:
                    print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)

compute_metrics()
