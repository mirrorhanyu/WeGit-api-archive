import re


def get_max_page(current_page, link_header):
    return max(re.findall(r'page=([0-9]+)>', link_header) + [current_page], key=int) if link_header else 0
