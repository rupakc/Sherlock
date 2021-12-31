def text_string_generator(text_string,iteration_size=12):
    start_index = 0
    stop_index = iteration_size
    for i in range(0,len(text_string),iteration_size):
        start_index = i
        stop_index = start_index + iteration_size
        yield text_string[start_index:stop_index]

text_string = "As part of developing the LogCollector tool, we are often faced with the issue of identifying Personally Identifiable Information from product log files.At the time of this writing, this is done in an ad-hoc manner where the log file or set of log files is sent to the legal team to verify if indeed they contain any personal attributes or not.This process is too cumbersome and often takes days or even weeks, sometimes causing inordinate delays in the development and deployment process.The idea behind Sherlock is to develop a generic service that can easily flag and anonymize personally identifiable information from a given file."

for text in text_string_generator(text_string):
    print(text)

file_path = '/Users/rupachak/Desktop/CCX Welcome/CCX Process (prev).log'

def read_in_chunks(file_object, chunk_size=8*1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield str(data)


with open(file_path,'r') as file:
    for c in read_in_chunks(file):
        print(c)


