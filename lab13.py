words = "The NOUN destroyed by a raging NOUN in New York's Trump Tower that VERB a resident and injured six firefighters had no sprinkler system, authorities said.Firefighters remained at the scene Sunday, cleaning up after the blaze and trying to determine its cause. The fire broke out shortly after 5 p.m. Saturday in the 58-story building.President Trump keeps a sprawling, penthouse residence in the building, and his business has offices there. Fire Commissioner Daniel Nigro said Secret Service agents accompanied firefighters to check on the Trump residence. Nigro said no Trump family members were inside.".split()

answers = []
for word in words:
  if word == "NOUN" or word == "VERB" or word == "ADJ":
    answers.append(word)

questions = ["Enter a noun:", "Enter a verb:", "Enter an adjective:"]
answers = []
for i in range(2):
  if answers[i] == "NOUN"
    answers[i] = raw_input(questions[0])
  elif answers[i] == "VERB"
    answers[i] = raw_input(questions[1])
  elif answers[i] == "ADJ"
    answers[i] = raw_input(questions[2])
    
wordCount = 0
for word in words:
  if word == "NOUN" or word == "VERB" or word == "ADJ":
    words.insert(answers[wordCount])
    wordCount += 1

print words