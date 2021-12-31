from piidetect.piiregex import *

# filepath = "/Users/rupachak/Desktop/CCX Welcome/CCX Process (prev).log"
# with open(filepath,'r') as f:
#     content = f.read()
#
# parsed_text = PiiRegex(content)
# print(parsed_text.text)
#
# print(parsed_text.dates)
# print(parsed_text.times)
# print(parsed_text.phones)
# print(parsed_text.phones_with_exts)
# print(parsed_text.emails)
# print(parsed_text.ips)
# print(parsed_text.ipv6s)
# print(parsed_text.guids)
# print(parsed_text.btc_addresses)
# print(parsed_text.street_addresses)
# print(parsed_text.postcodes)
# print(parsed_text.ukphones)
# print(parsed_text.paths)
# print(parsed_text.links)
# print(parsed_text.ssn)


def get_extracted_entities_from_string(pii_string, entity_to_extract_list):
    regex_names_supported = regexes.keys()
    extracted_regex_dict = dict({})
    for regex_name in entity_to_extract_list:
        if regex_name not in regex_names_supported:
            raise Exception("The following regex is not supported ", regex_name)
    for regex_name in entity_to_extract_list:
        extracted_regex_dict[regex_name] = regexes[regex_name].findall(pii_string)
    return extracted_regex_dict


import re

# s = "C:\\Users\\vdhiman\\AppData\\Roaming\\Adobe\\CCX Welcome\\learn\\PHXS-21.2.1"

s = "/Users/vdhiman/AppData/Roaming/Adobe/CCX Welcome/learnhello my dear friend charlie how are you doing C:\\Users\\vdhiman\\AppData\\Roaming\\Adobe\\CCX Welcome\\learn\\PHXS-21.2.1" \
    "rupachak@adobe.com +91 9830303145 http://www.thequantumexplorer.org"

test_paths = re.compile(r'((((?<!\w)[A-Z,a-z]:)|(\.{1,2}\\))([^\b%\/\|:\n\"]*))|("\2([^%\/\|:\n\"]*)")|((?<!\w)(\.{1,2})?(?<!\/)(\/((\\\b)|[^ \b%\|:\n\"\\\/])+)+\/?)', re.IGNORECASE)
paths = re.compile(r'''^['"]?(?:/[^/]+)*['"]?$''',re.DOTALL | re.VERBOSE| re.IGNORECASE)

results = paths.findall(s)
print(results)

# entity_to_extract_list = ['emails','ips','ipv6s','phones','links','paths','ssn']
#
#
# import pprint
# pprint.pprint(get_extracted_entities_from_string(s,entity_to_extract_list))
