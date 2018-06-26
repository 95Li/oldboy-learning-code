import  re
# print(re.findall('\w\W','_&%12 we 2&_ 2'))
# print(re.findall('\W','_&%12 we 2&_ 2'))
# print(re.findall('\s','_&%12 \twe\r 2&_ 2'))
# print(re.findall('\S','_&%12 \twe\r 2&_ 2'))
# print(re.findall('\d','_&%12 we 2&_ 2'))
# print(re.findall('\D','_&%12 we 2&_ 2'))

# print(re.findall('\Aalex','alex is  alex nb'))
# print(re.findall('alex\Z','alex is  alex'))
# print(re.findall('^alex','alex is  alex nb'))
# print(re.findall('^alex$','alex'))


# print(re.findall('.ab','a ab abb abbb'))
# print(re.findall('b?a*b','a ab abb baaaaaabbb'))
# print(re.findall('a?b','a ab abb aaaaabbb'))
# print(re.findall('a.b','a ab abb abbb'))

# print(re.findall('a.*b','a ab a\nbb abbb'),re.DOTALL)   #贪婪匹配
# print(re.findall('a.*?b','a ab a\nbb abbb'),re.DOTALL)  #非贪婪匹配
# print(re.findall('ab｛0，1｝','a ab abb abbb'))
# print(re.findall('b.*b.*b','aboooooboobbasd'))
# print(re.findall('b.*b.*','abooooooobbasd'))

# print(re.findall('([a-z]+)_sb','egon ab_sb 23423asd_sb wxxxxxxx_sb'))
# print(re.findall('[^a-zA-Z0-9]','egon ab_sb 2'))
# print(re.findall('[a-zA-Z]+[a-zA-Z0-9]{7,9}','A123DSGAF'))、



