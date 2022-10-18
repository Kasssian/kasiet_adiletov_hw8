import re

content = ['+996502000103', '+996508444433', '+996755800000', '+996778734145']
content_string = ""
for i in content:
    content_string += i + ' '
beeline = re.findall(r"\+996(?:77\d|22\d)\d{6}", content_string)
print(beeline)
megacom = re.findall(r"\+996(?:55\d|99\d|755)\d{6}", content_string)
print(megacom)
o = re.findall(r"\+996(?:50\d|70\d)\d{6}", content_string)
print(o)
