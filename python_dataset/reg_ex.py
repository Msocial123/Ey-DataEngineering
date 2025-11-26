import re #1
# text='ABC 123 XYZ 456 _@&! 100 2000'
#
# # pattern=re.compile(r'\d\d\d') #2
# # matches=pattern.search(text) #3
# # print(matches)
#
# pattern=re.compile(r'(\d{3})') #2
# matches=pattern.finditer(text) #3
# for match in matches:
#     print(match.group())

# text = '''
# Hi, today is 17-Apr-2021, yesterday was 16-Apr-2021 and tomorrow will be 18-Apr-2021.
# My schedule is free on 26-04-2021, 06.05.2021 and 16/Jun/2021.
# You can reach out to me at myname2020@dummy.com or ask_help@demo.net & conference@demo.co.in
# You can also call me at one of the following no’s +6032-007 1212, +6099.100 3344, 017-9998800 etc.
# '''
#
# # date_pattern=re.compile(r'\d{2}-[a-zA-Z]{3}-\d{4}')
# #date finding pattern
# date_pattern=re.compile(r'\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}')
# matches=date_pattern.finditer(text)
# for match in matches:
#     print(match.group())
#
# #email finding pattern
# email_pattern=re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+')
# matches=email_pattern.finditer(text)
# for match in matches:
#     print(match.group())
#
# #phone finding pattern
#
# phone_pattern=re.compile(r'(\+\d)?\d{3}[-.]\d{3}\s?\d{4}')
# matches=phone_pattern.finditer(text)
# for match in matches:
#     print(match.group())


# text='Hi Hi dfdsfdsfdsfdsffdsf?'
# pattern=re.compile(r'^(H).*\?$')
# matches=pattern.finditer(text)
# for match in matches:
#     print(match.group())


# re.sub(pattern, repl, text) — replace matches.
text='my income in 2020 was $20,000, but now it is $25,0000'
pattern=re.compile(r'\$[0-9,]+')
matches=pattern.sub('*******************************',text)
print(matches)