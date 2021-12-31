import re
from constants import commonconstants
from piidetect import piiregex


def anonymizing_pipeline(text_string, anon_entity_list):
    """
    Matches the text string with a set of pre-defined regexes and anonymizes the same

    :param text_string: text containing the PII which needs to be replaced
    :return: String containing the PII removed
    """

    if anon_entity_list is None or len(anon_entity_list) == 0:
        anon_entity_list = commonconstants.ANON_ENTITY_DICT.keys()
    anon_text = text_string
    for anon_entity in anon_entity_list:
        anon_text = re.sub(piiregex.regexes[anon_entity], commonconstants.ANON_ENTITY_DICT[anon_entity], anon_text)
    return anon_text


def filter_path_false_positives(path_string):
    """
    Given a path string the function attempts to filter out the false positives using heuristics

    :param path_string: String containing the path to validate
    :return: True if it is a valid path, False otherwise
    """
    if len(path_string) < 10:
        return False
    count_backward_slash_separator = path_string.find("\\")
    count_forward_slash_separator = path_string.find("/")
    count_newline_separator = path_string.find("\\n")
    domain_extension_list = ['.com', '.io', '.in', '.de', '.us', '.org', '.gov', '.net']
    if any(domain_extension in path_string for domain_extension in domain_extension_list):
        return False
    if count_newline_separator > 0:
        return False
    if count_forward_slash_separator > 0 or count_backward_slash_separator > 0:
        return True
    return False
