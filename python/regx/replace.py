import re

text = "The quick brown fox"
pattern = r"quick"
replacement="set"
replace=re.sub(pattern, replacement, text)
print(replace)