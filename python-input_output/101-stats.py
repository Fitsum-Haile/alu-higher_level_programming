#!/usr/bin/python3
"""
This script reads input line by line from stdin
and computes metrics based on the input format:
"""

import sys


def parse_line(line):
    """Parse each line of input and extract status code and file size."""
    parts = line.split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size


def print_statistics(total_size, status_counts):
    """Print current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                status_code, file_size = parse_line(line)
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)

            except ValueError:
                continue

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

    print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
