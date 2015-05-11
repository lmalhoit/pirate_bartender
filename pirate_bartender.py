import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def drink(questions):

  answers = {}

  for key,value in questions.iteritems():
    print value
    answer = raw_input()
    if answer == "y" or answer == "yes":
      answer = True
    else:
      answer = False
    answers[key] = answer
  
  return answers  

def pour(answers, ingredients):
  ingredients_list = []
  
  for key, value in answers.iteritems():
    if value == True:
      ingredients_list.append(random.choice(ingredients[key]))
  return ingredients_list

def cocktail_name(answers):
  first_adj = ["slimey", "subtle", "blue", "dirty", "steamy"]
  second_noun = ["dog", "pig", "foot", "cleaner", "closer"]
  
  print "How about a {} {}?" .format(random.choice(first_adj), random.choice(second_noun)) 
  

if __name__ == '__main__':

  drink_input = "y"
  while drink_input == "y":
    print "How about a drink? y/n"
    drink_input = raw_input()
    if drink_input == "y":
      answers = drink(questions)
      print answers
      ingredients_list = pour(answers, ingredients)
      print ingredients_list
      cocktail_name(answers)
    else:
      print "Lightweight!"