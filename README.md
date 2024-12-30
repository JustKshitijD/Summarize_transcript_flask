Add your Gemini 1.5 flash key to app/utils.py

This can be run by - "python3 run.py".
Run tests from tests/ folder-
1) python3 test1.py:- Summarizes earning transcript of earning_call_dr_lal_pathlabs.
2) python3 test2.py:- Summarizes earning transcript of earning_call_one97.
3) python3 test3.py:- company_name field is empty in input json. This should return "No company_name provided".
4) python3 test4.py:- transcript_text field is empty in input json. This should return "No transcript_text content provided".
5) python3 test5.py:- company_name field is not present in input json. This should return "No company_name provided".
6) python3 test6.py:- transcript_text field is not present in input json. This should return "No transcript_text content provided".

summarize_earning.ipynb is the notebook downloaded from Google Colab runs of this code.
All these tests (local tests and PythonAnywhere tests for both Dr Lal Pathlabs and One97 are run there - normal cases and error handling cases). 
