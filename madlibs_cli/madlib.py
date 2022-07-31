import re

print('Welcome to the madlibs generator!')
print('Please enter a sentence:')
adjective1 = input('Give me an adjective: ')
adjective2 = input('Give me another adjective: ')
noun = input('Give me a noun: ')

print("It was a " + adjective1 + " and " + adjective2 + " " + noun + ".")

input_tuple = (adjective1, adjective2, noun)

regex = r"(?<={).*?(?=})"

with open ('assets/dark_and_story_night_template.txt') as file:
  read_template = file.read().strip()
print(read_template)
file.close()

speech_parts = re.findall(regex, read_template)
parsed_message = re.sub(regex,'', read_template)
completedMadlib =  parsed_message.format(adjective1, adjective2, noun)
print(completedMadlib.format)

def merge(b, **a):
  print(a)
  print(b)
  new_sentence = a.format(b)
  return new_sentence

# madlib = merge(read_template, input_tuple)
# print(madlib)

file = open('assets/dark_and_story_night_template.txt', 'w')
n = file.write(completedMadlib)
file.close()