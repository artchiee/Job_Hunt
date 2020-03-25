import re
href = ['https://ma.indeed.com/emplois?q=php&rbl=Casablanca&jlid=b2cb1aaecdd05390',
        'https://ma.indeed.com/emplois?q=php&rbl=Rabat&jlid=d8946cbfa6e79760']
href_pattern = re.compile(r"^\=[a-zA-Z]\+&$")
new_href = list(filter(href_pattern.match, href))
x = input(str('Something : '))
for me in href:
    if x in me:
        print('found url : ', x)
    else:
        print('error')
