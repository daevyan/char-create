def get_gender_pronoun(answer):
    print "Got gender pronoun answer is: %s." % answer
    answer = str(answer)
    if answer == 'male':
        pronoun = ["he", "him", "his"]
    elif answer == 'female':
        pronoun = ["she", "her", "hers"]
    else:
        pronoun = None
        print "Cannot set pronoun"
    print pronoun
    return pronoun

get_gender_pronoun(raw_input('>'))
