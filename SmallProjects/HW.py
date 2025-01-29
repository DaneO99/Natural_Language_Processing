import re
txt = "The rain in Spain falls mainly on the plains."
print(re.findall(".ain", txt))
#rain, pain, main, lain
print(re.findall("[a-z]+ain", txt))
#rain, pain, main , plain
print(re.findall("[A-Z]*[a-z]+ain[a-z]*", txt))
#rain, Spain, mainly, plains
print(re.findall(".*ain", txt))
name = "Mika Morgan"

#Write code that will search "name" and print all letters within "name"
#Only print letters, not any whitespace
print(re.findall("\w", name))
phone_number = " 2(3)13-82 (123)456-7890 987654321"

#Write code that will search "phone_number" and print valid phone numbers within the text
#Valid phone numbers have parentheses with exactly 3 numbers, followed by exactly 3 numbers, -, and 4 numbers

#Note: be careful of looking for special characters in regex...
print(re.findall("\(\d{3}\)\d{3}-\d{4}", phone_number))
email = "random@wrong mikamorgan@msutexas.edu random@correct.com"

#Write code that will search "email" and print valid emails within the text
#Valid emails have any number of alphanumeric characters followed by an "@" symbol, followed by any
#number of alphanumeric characters, followed by a "." and exactly 3 letters

#Note: be careful of looking for special characters in regex...
print(re.findall("\w+@\w+\.\w{3}", email))
numbers = "$30.92 7,984 $22f one million dollars $4.61 $83.1 $20040.57 $300"

#Write code that will search "numbers" and print valid USD amounts within the text
#Valid dollar amounts start with a $, followed by any number of digits, then a
#period, and end with exactly 2 decimal places

#Note: be careful of looking for special characters in regex...
print(re.findall("\$\d+(?:\.\d{2})?",numbers))
txt = '''We hold these truths to be self-evident, that all men are created equal,
         that they are endowed by their Creator with certain unalienable Rights,
         that among these are Life, Liberty and the pursuit of Happiness.'''

#Write a code block that will search "txt" and count the number of times the word
#"the" appears. Disregard words that have "the" embedded within, such as
#"these," "their," and "they" etc.
print(re.findall("the\s", txt))