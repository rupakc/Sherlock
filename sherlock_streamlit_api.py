import streamlit as st
from piidetect.piiregex import *
from utils import commonutils


entity_to_extract_list = ["emails", "ips", "ipv6s", "phones", "dates", "times", "links", "paths", "ssn", "guids"]


def read_in_chunks(file_object, chunk_size=8*1024):
    """
    Lazy function (generator) to read a file piece by piece. Default chunk size is 8k.

    :param file_object - Object containing the file handler
    :param chunk_size - Integer specifying the chunk size in bytes
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield str(data)


def filter_detected_pii_for_false_positives(extracted_regex_dict, pii_entity_list):
    if "paths" in pii_entity_list:
        extracted_regex_dict["paths"] = list(filter(commonutils.filter_path_false_positives, extracted_regex_dict["paths"]))
    return extracted_regex_dict


def get_extracted_entities_from_string(pii_string,pii_entity_list):
    """
    Function to extract the personally identifiable information from a string

    :param pii_string - String containing text to detect PII from
    :param pii_entity_list - List specifying the type of PII entities to detect
    """
    if len(pii_entity_list) == 0:
        pii_entity_list = entity_to_extract_list
    regex_names_supported = regexes.keys()
    extracted_regex_dict = dict({})
    for regex_name in pii_entity_list:
        if regex_name not in regex_names_supported:
            raise Exception("The following regex is not supported ", regex_name)
    for regex_name in pii_entity_list:
        extracted_regex_dict[regex_name] = list(set(regexes[regex_name].findall(pii_string)))
    filtered_regex_dict = filter_detected_pii_for_false_positives(extracted_regex_dict, pii_entity_list)
    return filtered_regex_dict


def anonymize_pii_information(text_string, anon_entity_list):
    """
    Function to anonymize the personally identifiable information from text string

    :param text_string - String containing the text to anonymize
    :param anon_entity_list - List specifying the type of PII to anonymize
    """
    return commonutils.anonymizing_pipeline(text_string, anon_entity_list)


st.title("Sherlock - A Service for Detecting and Anonymizing PII")
st.header('Please Select the Type of Operation you would like to Perform')
workflow = st.radio('Please Make a selection',('Detect PII in my text','Anonymize the PII in my text'))
text_string_input = ''
file_object = None

st.sidebar.header("About the App")
st.sidebar.success('As part of developing the LogCollector tool, we are often faced with the issue of identifying Personally Identifiable Information from product log files.'
                   'At the time of this writing, this is done in an ad-hoc manner where the log file or set of log files is sent to the legal team to verify if indeed they contain any personal attributes or not.'
                   'This process is too cumbersome and often takes days or even weeks, sometimes causing inordinate delays in the development and deployment process.'
                   'The idea behind Sherlock is to develop a generic service that can easily flag and anonymize personally identifiable information from a given file.')

if workflow == 'Detect PII in my text':
    input_choice = st.radio('What would you prefer?', ('Enter Free Text', 'Upload a Log File'))
    pii_entity_list = st.multiselect('Choose the types of PII to detect',
                                     ["emails", "ips", "ipv6s", "phones", "dates", "times", "links", "paths", "ssn", "guids"],
                                     default=["emails", "ips", "links", "guids", "paths"])
    if input_choice == 'Enter Free Text':
        text_string_input = st.text_area('Enter the text you would like to detect PII from', height=500)
    else:
        file_object = st.file_uploader(label="Upload the file to analyze")
    if st.button("Detect PII Now"):
        with st.spinner():
            if input_choice == 'Upload a Log File':
                for chunk_data_string in read_in_chunks(file_object):
                    extracted_json_pii_dict = get_extracted_entities_from_string(chunk_data_string, pii_entity_list)
                    st.success("Successfully Detected PII from your data")
                    st.json(extracted_json_pii_dict)
            else:
                extracted_json_pii_dict = get_extracted_entities_from_string(text_string_input, pii_entity_list)
                st.success("Successfully Detected PII from your data")
                st.json(extracted_json_pii_dict)
else:
    input_choice = st.radio('What would you prefer?', ('Enter Free Text', 'Upload a Log File'))
    anon_entity_list = st.multiselect('Choose the types of PII to anonymize',
                                     ["emails", "ips", "phones", "links", "paths", "guids"],
                                     default=["emails", "ips", "links", "guids", "paths"])
    if input_choice == 'Enter Free Text':
        text_string_input = st.text_area('Enter the text you would like to anonymize', height=500)
    else:
        file_object = st.file_uploader(label="Upload the file to analyze")
    if st.button("Anonymize PII Now"):
        with st.spinner():
            if input_choice == 'Upload a Log File':
                for text_string_chunk in read_in_chunks(file_object):
                    anon_text = anonymize_pii_information(text_string_chunk, anon_entity_list)
                    st.success(anon_text)
            else:
                anon_text = anonymize_pii_information(text_string_input, anon_entity_list)
                st.success(anon_text)
