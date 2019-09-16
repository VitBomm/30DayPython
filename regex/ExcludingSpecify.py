Regex_Pattern = r'^\D[^ueoai][^bcDF][^\r\n\t\f ][^UEOAI][^.,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())