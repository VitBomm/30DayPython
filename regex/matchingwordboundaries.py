Regex_Pattern = r'\b[UEOAIueoai][A-Za-z]{0,}\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())