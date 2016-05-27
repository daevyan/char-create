from question import Question
from answer import Answer
from validator import *


class Looks(object):

    """ -------------------- Lists --------------------"""

    gender_list = ["male", "female"]

    """Body:"""
    height_list = ["very tall", "a little taller than average", "of average height", "a little shorter than average", "very short"]
    build_list = ["small-boned", "medium, solid", "soft, tending to rounded"]
    weight_list = ["emaciated", "underweight", "slightly underweight", "average weight", "slightly overweight", "overweight", "obese"]
    skin_details = ["burned", "flushed", "freckled", "pocked", "reddened", "rough", "sallow", "sickly", "smooth", "tanned", "wrinkled",
                    "acne scars", "a birthmark", "a scar", "a mole"]
    skin_color = ["light-pale", "light-olive", "light-ruddy", "medium-brown", "medium-olive", "medium-ruddy", "dark-brown", "dark-olive",
                  "dark-ruddy", "dark-black"]
    additional_details = ["tattoo", "piercing"]

    """Face"""
    face_shape = ["diamond-shape face", "heart-shape face", "long face", "oval face", "round face", "square face"]
    forehead = ["broad forehead", "creased brow", "high forehead", "receding hairline", "widow's peak", "lined forehead", "smooth forehead"]
    eye_color = ["amber", "dark brown", "light brown", "green", "light blue", "dark blue", "blue-green", "gray", "hazel-green",
                 "hazel-brown", "hazel-blue", "heterochromatic", "milky"]
    eye_details = ["angled", "almond", "bagged", "bulging", "close-set", "deep-set", "single-lidded", "large", "shadowed", "reddened", "round", "small",
                   "squinty", "sunken", "watery", "wide-set", "wrinkled"]
    eyebrows = ["arched", "bushy", "dark", "fair", "shaved", "thin", "unibrow"]
    nose = ["broken", "bulbous", "crooked", "flat", "hawk", "hooked", "large", "wide", "narrow", "bent", "short", "small", "snub",
            "turned-up"]
    lips = ["chapped", "cleft palate", "bitten", "curled-down", "curled-up", "full", "large", "puffy", "stained", "thin", "firm"]
    chin = ["recessed chin", "strong jaw", "jowls", "jutting chin", "double chin", "chin cleft"]
    face_details = ["smile lines", "high cheekbones", "dimple", "frown lines", "prominent adam's apple", "sunken cheeks", "thick neck",
                    "round cheeks"]
    facial_hair = ["beard", "goatee", "mustache", "mustache, pencil", "mustache, walrus", "mutton-chops", "sideburns", "soul patch",
                   "stubble", "van dyke"]

    """Hair"""
    hair_color = ["light blond", "dark blond", "strawberry blond", "medium red", "auburn", "light brown", "medium brown", "dark brown",
                  "black-brown", "black-blue", "silver", "gray", "salt-and-pepper", "bright red", "bleached blond", "copper", "pink",
                  "violet", "blue", "green", "platinum blond", "ash blond", "jet black"]
    hair_color_details = ["colorful streaks", "single streak", "lowlights", "highlighted", "visible roots/dye-line"]
    hair_type = ["coarse", "curly", "curly (permed)", "fine", "frizzy", "chemically straightened", "straight", "thick", "thin", "wavy",
                 "wiry"]
    hair_length = ["stubble", "cropped", "short", "chin-length", "shoulder-length", "elbow-length", "waist-length"]

    """
    ----------------- Ideas for questions -----------------

    eyes: eye_color, eye_shape
    hair: hair_color, hair_type, hair_length
    face: nose, lips, cheekbones, face_shape, marks (freckles, moles, scars, etc.), facial_hair
    Body: build, skin_color, marks (freckles, moles, scars, etc.), weight, build
    Other: voice, smell, clothes_style, other (open, like: (eyebrows, lashes, makeup, facial hair color, large hands, small hands, ...)

    basic - eye_color, hair_color, hair_type, hair_length, skin_color, marks, weight, build, facial_hair (for males), other, voice
    adv - all
    """

    """ -------------------- Questions --------------------"""

    appearance_questions = [
        Question("name", "Let's start with naming your character:",
                 "Ok, so let's get on with it! We'll start with %s's Looks, than go through\n"
                 "Personality, and finish with some kind of Background.\n" % Answer().char_appearance.get("name"),
                 EmptyValidator()
                 ),
        Question("gender", "Ok, what is %s's gender?" % Answer().char_appearance.get("name"),
                 "Ah, a %s, OK." % Answer().char_appearance.get("gender"),
                 GenderValidator(gender_list),
                 ),
        Question("age", "And how old is your character?",
                 "So, your character is a %s years old." % Answer().char_appearance.get("age"),
                 AgeValidator()
                 ),
        Question("height", "Describe the height of your character",
                 "Confirmation: %s" % Answer().char_appearance.get("height"),
                 EmptyValidator(),
                 height_list
                 ),
        Question("build", "How is your character build?",
                 "Confirmation: %s" % Answer().char_appearance.get("build"),
                 EmptyValidator(),
                 build_list
                 ),
        Question("weight", "Describe the weight of your character",
                 "Confirmation: %s" % Answer().char_appearance.get("weight"),
                 EmptyValidator(),
                 weight_list
                 )

    ]

    def get_range(self, value, range_dict):
        for range_name, range_value in range_dict.iteritems():
            if value in range_value:
                return range_name
        raise ValueError("Something, somwhere went awfully wrong. Sorry. %r not a value I can take."
                         % value)


class Personality(Question):
    pass


class Background(Question):
    pass