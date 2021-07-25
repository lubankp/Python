# find word in sentence

list_of_sentences = ['Three pounds of self-rasing flour',
                     'Two pounds of plain flour',
                     'Six ounces of butter']

for i, sentence in enumerate(list_of_sentences):
    pos = sentence.find('pounds')
    if pos > 0:
        print(f"pound find at position {pos} in sentence {i+1}")
    else:
        print(f"pound not find in sentence {i+1}")