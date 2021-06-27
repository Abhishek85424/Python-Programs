import re
st = " My      string     is this"
st = re.sub('\s+',' ',st)
print(st.strip())