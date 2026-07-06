import re
text="uma test shankar"
pattern=r" "
new= re.split(pattern, text)
print("print", new)

import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)