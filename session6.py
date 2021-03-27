#regexp
import re
unknown= "This is the I have been waiting for, I need to revel in it"
match = re.match(r 'have', '(.*)', 'waiting', unknown)
print(match)