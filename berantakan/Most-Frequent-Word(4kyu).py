import re

def top_3_words(text):
    text = text.lower()
    list_of_word = re.split(r"[^a-zA-Z0-9']+", text)
    list_of_word = [segment for segment in list_of_word if segment]
    
    most_word = ['_' for _ in range(len(list_of_word))]
    require_count = [0 for _ in range(len(list_of_word))]
    
    used_word = []
    final_result = {}
    
    for word in list_of_word:
        if word not in used_word:
            used_word.append(word)
            counter = list_of_word.count(word)
            minimal = min(require_count)
            if counter > minimal:
                index_to_change = require_count.index(minimal)
                most_word[index_to_change] = word
                require_count[index_to_change] = counter
    
    for key, value in zip(most_word, require_count):
        final_result[value] = key
    
    sorted_final_result = sorted(final_result.items(), reverse=True)
    
    return [item[-1] for item in sorted_final_result]

# print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to \
# mind, there lived not long since one of those gentlemen that keep a lance \
# in the lance-rack, an old buckler, a lean hack, and a greyhound for \
# coursing. An olla of rather more beef than mutton, a salad on most \
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra \
# on Sundays, made away with three-quarters of his income."))

# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words(''))