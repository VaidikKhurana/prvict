from test_main import *


def contextual_sim_test(input):
   intent_categories = [["hello", "hi", "sup", "yo"], ["bye","peace out", "cya", "see you", "goodbye"]]
   greeting_intent = intent_categories[0]
   outcome_probability = []
   bye_intent = intent_categories[1]
   intent_outcomes = []
   for category in intent_categories:
      for word in category:
         similarity_word = sim(word, input)
         if word == input or  similarity_word>= 90:
            intent_outcomes.append(word)
            outcome_probability.append(similarity_word)
   outcome = intent_outcomes[outcome_probability.index(max(outcome_probability))]
   print(outcome)  



def contextual_sim_testw(input):
   intent_categories = [["hello", "hi", "sup", "yo"], ["bye","peace out", "cya", "see you", "goodbye"]]
   greeting_intent = intent_categories[0]
   peace_intent = intent_categories[1]
   outcome_category = []
   for category in intent_categories:
      for word in category:
         if word == input or sim(word, input) >= 70 or sim(input, word) >= 70:
            outcome_category.append(category)

   return outcome_category


print(contextual_sim_testw("goodby"))