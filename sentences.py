import random

def main():
    """
    This is the main app.
    """
        
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    if quantity == 1:
        determiner = get_determiner(1)
        noun = get_noun(1)
        preposition = get_prepositional_phrase(1)
    else:
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        preposition = get_prepositional_phrase(quantity)
        # Get a list of verbs
    
    if tense == "past":
        verb = get_verb(quantity, "past")
    elif tense == "present" and quantity == 1:
        verb = get_verb(1, "present")
    elif tense == "present":
        verb = get_verb(quantity, "present")
    elif tense == "future":
        verb = get_verb(quantity, "future")
        
    return f"{determiner.capitalize()} {noun} {verb} {preposition}."
        
        
        
        

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
    
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        single = [ "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        single_noun = random.choice(single)
        return single_noun
    else:
        plural = [ "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        plural_nouns = random.choice(plural)
        return plural_nouns    
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    if tense.lower() == "past":
        past = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        past_verb = random.choice(past)
        return past_verb
    elif tense.lower() == "present" and quantity  == 1:
        present = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
        present_verb = random.choice(present)
        return present_verb
    elif tense.lower() == "present" and quantity != 1:
        present = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        present_verb = random.choice(present)
        return present_verb
    elif tense.lower() == "future":
        future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        future_verb = random.choice(future)
        return future_verb

    # Add Get Preposition Functions Below and call within the main function above.
def get_preposition():
    """
    Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    preposition_list = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(preposition_list)
    return preposition
        
def get_prepositional_phrase(quantity):
    """
    Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    noun = get_noun(quantity)
    determiner = get_determiner(quantity)
    preposition = get_preposition()
    prepositional_phrase = f"{preposition} {determiner} {noun}"
            
    return prepositional_phrase
    
main()