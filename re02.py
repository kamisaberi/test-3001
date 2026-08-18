import re

username = "ali123"

k = bool(re.search("^[a-zA-Z0-9_]+$", username))
print(k)