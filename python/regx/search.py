import re
text="uma shankar test"
pattern=r"na"
search=re.search(pattern, text)

if search:
    print("search found", search.group())
    print("search index start", search.start())
    print("search end index", search.end())
else:
   print("not found")