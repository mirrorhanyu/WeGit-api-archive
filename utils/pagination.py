import re


def get_max_page(link_header):
    if link_header:
        max_page_in_header = max([int(number) for number in re.findall(r'page=([0-9]+)>', link_header)])
        return max_page_in_header if 'rel="last"' in link_header else max_page_in_header + 1
    else:
        return 0
