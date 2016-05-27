class Personality(object):

    """
    The Basic Profile
    """
    primary_motivators_desc = "In the broadest sense, the Primary Motivator is the underlying engine of your character's life." \
                              "It is the foundational theme of his worldview and, at a deep level, is what ultimately drives him to action." \
                              "While any given act might be tactically pragmatic in service to short-term goals, the PM is there in the" \
                              "background influencing his aims and behaviors."
    primary_motivators = ["achievement", "acquisition", "adoration", "balance/peace", "beneficence", "chaos", "competition", "conflict",
                          "conquest", "corruption", "creation", "destruction	discovery/adventure", "domesticity", "education",
                          "entertainment", "enslavement", "hedonism", "heroism", "liberation", "love", "nobility/honor", "order", "play",
                          "power", "proselytization", "purity", "rebellion", "recognition", "service", "torment", "understanding", "vice"]

    primary_motivators_dict = {
        "achievement": "To overcome obstacles and succeed; to become the best",
        "acquisition": "To obtain possessions/wealth",
        "adoration": "To be cherished, admired, and wanted by others",
        "balance/peace": "To bring all things into harmony and equilibrium",
        "beneficence": "To protect the helpless, heal the sick, feed the hungry, etc.",
        "chaos": "To disrupt, to cause confusion and discord",
        "competition": "To seek out or create rule-based win/lose scenarios; to defeat others in contests",
        "conflict": "To seek out or create rivalry, fighting, or animosity",
        "conquest": "To conquer other peoples, to bring them into one's own culture/rule",
        "corruption": "To despoil, ruin, humiliate, or make depraved",
        "creation": "To build or make new, such as art, culture, invention, design,etc.",
        "destruction": "To annihilate, exterminate, and unmake",
        "discovery/adventure": "To explore, uncover mysteries, and pioneer",
        "domesticity": "To get married, have children, and live a family life",
        "education": "To provide information, teach, enlighten, or train",
        "entertainment": "To entertain, amuse, and delight others",
        "enslavement": "To force others into servitude",
        "hedonism": "To enjoy all things sensuous",
        "heroism": "To find valor and honor through battle or self-sacrifice",
        "liberation": "To free the self and/or others from perceived captivity or enslavement",
        "love": "To experience/share affection and emotional commitment, whether romantic or platonic",
        "nobility/honor": "To exalt ideals such as generosity, honesty, bravery, and courtliness",
        "order": "To arrange, organize, and reduce chaos",
        "play": "To have fun, to enjoy life",
        "power": "To control and lead others",
        "proselytization": "To spread a belief system; indoctrinate others",
        "purity": "To achieve a state of moral or spiritual perfection, of self and/or others",
        "rebellion": "To fight against power structures; to undermine authority",
        "recognition": "To gain approval, social status, or fame",
        "service": "To follow a person, government, order, religion, etc.",
        "torment": "To inflict pain and suffering, on others and/or the self",
        "understanding": "To seek knowledge or wisdom (spiritual, scientific, magical,etc)",
        "vice": "To enable or engage in self-destructive behavior"
    }

    emotional_disposition_desc = "The ED describes the general emotional set or 'resting state' of the character. This doesn't mean that" \
                                 "the character is limited to the ED, it just informs you of the emotion the character is most likely" \
                                 " to be experiencing at any given time. This trait can be used to help you determine how your character" \
                                 "is likely to emotionally respond to a situation, as well as how she appears to others." \
                                 "For instance, a primarily joyous person will act and speak differently than one who tends" \
                                 "towards anxiety or contempt." \
                                 "Finally, don't make the mistake of correlating the ED with alignment - " \
                                 "it is possible to be joyously evil and angrily good."
    emotional_disposition = ["joyful", "anxious", "melancholy", "curious", "calm", "angry", "contemptuous", "excited", "apathetic", "ashamed"]
    moodiness_desc = "Moodiness describes how easily one feels strong emotion. It's basically the level of emotional stability." \
                     "Labile describes being quick to experience strong emotions and Phlegmatic describes being emotionally steady and low-key."
    moodiness = ["labile", "even-tempered", "phlegmatic"]

    """
    Core Traits
    """
    core_traits_desc = "Where the Primary Motivator describes the global drive of your character, the Core Traits inform" \
                       "how a character is likely to act in any given situation. They help define how a character sees the world" \
                       "and how they move within it." \
                       "If you don't need much personality detail, picking out a Primary Motivator, the key Emotional Disposition," \
                       "and even one or two Core Traits should be enough to give any character a distinct flavor."
    core_traits_dict = {
        "outlook": "Outlook is one's basic worldview, interpreting the world as being essentially good or bad.",
        "integrity": "Basic values regarding work and social interactions.",
        "impulsiveness": "The ability to regulate one's thoughts and actions.",
        "boldness": "Willingness to face danger and enter into battle.",
        "agreeableness": "General attitude towards people and the ability to handle new situations, tough choices,"
                         "and interpersonal conflicts.",
        "interactivity": "Style and degree to which your character interacts with others.",
        "conformity": "Basic relationship with cultural norms"
    }
    outlook = {
        "optimistic": ["idealistic", "confident", "trusting", "hopeful", "upbeat"],
        "pessimistic": ["cynical", "bleak", "distrustful", "foreboding", "resigned"]

    }
    integrity = {
        "conscientious": ["industrious", "honest", "responsible", "meticulous", "pragmatic"],
        "unscrupulous": ["lazy", "deceitful", "unreliable", "manipulative", "slipshod", "impractical"]
    }
    impulsiveness = {
        "controlled": ["deliberate", "focused", "steady", "thoughtful"],
        "spontaneous": ["capricious", "flighty", "hyperactive", "rash"]
    }
    boldness = {
        "intrepid": ["daring", "reckless", "valorous", "dauntless", "audacious", "confident"],
        "cautious": ["timid", "paranoid", "vigilant", "nervous", "tentative"]
    }
    agreeableness = {
        "agreeable": ["warm", "empathic", "tolerant", "forgiving", "open-minded", "adaptable", "altruistic"],
        "disagreeable": ["cold", "rigid", "tense", "intractable", "narrow-minded", "cantankerous", "stingy"]
    }
    interactivity = {
        "engaging": ["talkative", "candid", "entertaining", "touchy"],
        "reserved": ["shy", "loner", "taciturn", "evasive", "cryptic"]
    }
    conformity = {
        "conventional": ["orthodox", "formal", "down-to-earth", "mainstream", "traditional"],
        "heterodox": ["rebellious", "arty", "shocking", "freethinking", "exotic"]
    }
    """
    Secondary Traits
    """
    sense_of_humor = ["crude", "dry", "slapstick", "jokey", "cynical", "prankster", "mean-spirited", "gleeful", "surreal", "none"]
    fav_conversation_topics = ["politics", "religion", "relationships", "work/profession/money", "entertainment-music, art, dance, games",
                               "hobbies and pastimes", "current events", "philosophy", "science", "humor"]
    fav_conversation_topics_desc = "What does your character like to talk about? It can be helpful to list out three or four topics" \
                                   "that your character defaults to in casual social situations. The basic rule of thumb is that people" \
                                   "like to talk about what they are good at and things they find interesting." \
                                   "So, look at your character's skills, hobbies, training, and background to see what he might be into." \
                                   "It's a good idea to come up with specifics, but some general topic areas to consider include: %s"\
                                   % ', '.join(fav_conversation_topics)
    group_affiliations_desc = "An optional component might be adding groups that your character identifies with. Affiliation plays" \
                              "an important role in how people actually act, and this can add another character dimension as well." \
                              "Quite simply, this comes down to deciding which general groups your character fits into and whose members" \
                              "he accepts as 'one of his own'." \
                              "For example, if your character enjoys playing dice, this can mean more than just the activity," \
                              "it can also mean identifying with dicers as a general group. A good place to start might be to look at" \
                              "your hobbies, any past professions, or religion. Also, after you finish your background, " \
                              "come back to this section and see if any groups pop out from your character's unique history."
    group_affiliations = []
    belief = ['agnosticism', 'buddhism', 'catholic church', 'christianity', 'deism', 'hinduism', 'islam', 'judaism', 'mormonism',
              'neopaganism', 'orthodox christianity', 'protestantism', 'sikhism', 'taoism']

    religiousness = ["non-believer", "agnostic", "casual adherent", "orthodox adherent"]
    """
    Quirks, Habits, and Oddities
    """
    oddities = ["animal hater", "beard/hair stroking", "belching", "blade sharpening", "chewing (e.g. sticks, small bones)",
                "coin flipping", "collects odd things", "compulsive lying", "constant eating", "constant grooming", "constant grooming",
                "counting", "dancing", "daydreaming", "eavesdropping", "exaggeration", "excessively touching others", "exhibitionism",
                "facial tics", "fingernail biting", "fingernail biting", "foot tapping", "hair pulling", "hair pulling", "humming",
                "insomnia", "knuckle cracking", "lip biting/licking", "mumbling", "name dropping", "name dropping", "needless apologizing",
                "nose picking", "pacing", "reciting poetry", "repeating others", "self-inflict pain/injury", "singing",
                "sleeping in odd places", "sleepwalking", "sleepwalking", "smelling things", "snacking (nuts, seeds, etc.)", "snoring",
                "stealing", "stuttering", "substance use (non-addicted)", "superstitious (omens, luck, etc.)", "talking in sleep",
                "teeth picking", "teeth picking", "teeth sucking", "tree climbing", "walking backwards", "whistling"]
