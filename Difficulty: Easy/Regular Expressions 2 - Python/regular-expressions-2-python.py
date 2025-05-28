import re
def validate(str):
    pat= re.compile(r"\w+\W+\d+")
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
