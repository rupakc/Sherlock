from fastapi import FastAPI, Body
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from piidetect.piiregex import *
from utils import commonutils

app = FastAPI()
security = HTTPBasic()
entity_to_extract_list = ["emails", "ips", "ipv6s", "phones", "dates", "times", "links", "paths", "ssn", "guids"]


@app.get("/v1/test/piidetect")
def get_extracted_entities_from_string(pii_string):
    """
    Function to extract the personally identifiable information from a string
    """
    regex_names_supported = regexes.keys()
    extracted_regex_dict = dict({})
    for regex_name in entity_to_extract_list:
        if regex_name not in regex_names_supported:
            raise Exception("The following regex is not supported ", regex_name)
    for regex_name in entity_to_extract_list:
        extracted_regex_dict[regex_name] = list(set(regexes[regex_name].findall(pii_string)))
    return extracted_regex_dict


@app.get("/v1/test/piianon")
def anonymize_pii_information(text_string):
    """
    Function to anonymize the personally identifiable information from text string
    """
    return commonutils.anonymizing_pipeline(text_string)
