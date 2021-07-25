# find word in sentence

list_of_sentences = ['Three pounds of self-rasing flour',
                     'Two pounds of plain flour',
                     'Six ounces of butter']

for i, sentence in enumerate(list_of_sentences):
    pos = sentence.find('pounds')
    with open('find_pound.txt', 'a') as f:
        if pos > 0:
            print(f"pound find at position {pos} in sentence {i+1}", file = f)
        else:
            print(f"pound not find in sentence {i+1}", file = f)