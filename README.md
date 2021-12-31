# Sherlock
A generic service for detecting personally identifiable information from log files

![architecture image][design]

[design]: https://github.com/rupakc/Sherlock/blob/main/Screenshot%202020-10-01%20at%205.47.58%20PM.png

As part of developing the <b> LogCollector tool </b>, we are often faced with the issue of identifying <b> Personally Identifiable Information </b> from product log files.At the time of this writing, this is done in an ad-hoc manner where the log file or set of log files is sent to the legal team to verify if indeed they contain any personal attributes or not.This process is too cumbersome and often takes days or even weeks, sometimes causing inordinate delays in the development and deployment process.The idea behind <b> Sherlock </b> is to develop a generic service that can easily flag and anonymize personally identifiable information from a given file.

## Steps to Run the Application

  - Install Python 3
  - Clone the repository
  - Install dependencies using ``` pip install -r requirements ```
  - Run the file ``` sherlock_streamlit_api.py ```
  

