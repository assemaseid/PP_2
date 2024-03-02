import re
#1 match string that has 'a' followeb by 0 or more 'b'

def match_string(input_string):
    pattern = re.compile(r'ab*')
    match = pattern.fullmatch(input_string)

    if match:
        print(f'"{input_string}" matched the pattern.')
    else:
        print(f'"{input_string}" not matched the pattern.')

strings = ['a', 'ab', 'abb', 'aabb', 'ac']
for test_string in strings:
    match_string(test_string)

#2 match 'a' followed by 2/3 'b'

pattern_2 = re.compile(r'a(b{2,3})')
strings = ['a','ab','abb','abbb','aBB','aBbB','abc','az']
for string in strings:
    if pattern_2.fullmatch(string):
        print(f'{string}: matched')
    else:
        print(f'{string}: not matched')


#3 matches in string in lower case with underscore
str = input( 'enter string:')
pattern_3 = r'^[a-z]+_[a-z]+$'
x = bool (re. search(pattern_3,str))
print(x)



#4 one uppercase followed by lower case
def text_match(text):
        pattern_4 = '[A-Z]+[a-z]+$'
        if re.search(pattern_4, text):
            print(f'{text}: matched')
        else:
            print(f'{text}: not matched')

text_match(input("Enter text:"))

#5 has 'a' followed by anything ending with 'b'

def match(string):
    pattern_5 = r'a.*?b$'
    if re.search(pattern_5, string):
        print(f'{string}: matched')
    else:
        print(f'{string}: not matched')

match(input("Enter:"))


# 6 replace dot, comma, space => colon
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))

# 7
def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))

#8
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))

# 9 insert space before cap letter
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))

#10 to convert camel string to snake case
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('PythonExercises'))

