# Starting code for our Flask web application

#
# Name(s):
#

import re
import json
import time

def substitute(old_text, dictionary_of_substitutions):
    """ our substitution engine:

        old_text: the body of text in which to make substitutions

        dictionary_of_substitutions:
          a Python dictionary with
            keys ~ the strings to replace (get rid of)
            values ~ the strings to replace the keys with! 

        return value, nex_text: the new text, with substitutions made!

        This is the function to change, to create xkcd-type substitutions!
    """
    # dictionary_of_substitutions = dictionary_of_substitutions
    print(f"dictionary_of_substitutions: {dictionary_of_substitutions}")
    new_text = old_text

    for s in dictionary_of_substitutions:
        string_to_replace = s
        # print(string_to_replace)
        replacement = dictionary_of_substitutions[s]
        # print(replacement)
        new_text = re.sub( string_to_replace, replacement, new_text )
        # print(new_text)

    # use re.sub
    
    
    # return the result
    return new_text



def seconds_since_1970(input=''):
    """ returns a json structure with two key-value pairs:
            'seconds': <the floating-point # of seconds since 1/1/1970>
            'origin': '1/1/1970'

        the input isn't used, but could be in the future
    """
    elapsed_seconds = time.time()  # built-in, counts seconds since 1970

    d = { 'seconds': elapsed_seconds, 
          'origin' : '1/1/1970' }

    string_version = json.dumps(d)  # using the json library to "dump" a string

    return string_version

    # then, try grabbing this json data -- using requests!

    


# Function takes in a string, and returns on which has been 
# translated into pig latin
def pig_translate(S):
    """ pig latin converter from '19 (with thanks to Justin G.!) """
    retStr = ''
    V = ['a','A','e','E','i','I','o','O','u','U']
    currFront = S[0]
    seen_vowel = False
    for i in range(len(S)):
        if S[i] == ' ':
            if currFront in V:
                retStr += 'yay '
            else:
                retStr += currFront.lower() + 'ay '
        elif i == len(S)-1:
            if currFront in V:
                retStr += S[i]+ 'yay'
            else:
                retStr += S[i] + currFront.lower() + 'ay'
        else:
            if S[i-1] == ' ' or i == 0:
                seen_vowel = False
                currFront = S[i]
                if currFront in V:
                    retStr += S[i]
                    seen_vowel = True
            else:
                if S[i] in V:
                    seen_vowel = True
                    retStr += S[i]
                else:
                    if not seen_vowel:
                        currFront += S[i]
                    else:
                        retStr += S[i]
    return retStr


# import what3words
# import requests

# #
# # web-access 1
# # my API key AFRG9VHR
# #

# def convert_to_coordinates(words):
#     """ convert_to_coordinates takes in one string
#         words: the word triple that we are trying to find the location of
        
#         it will return a string of the coordinates described by the word triple

#         my html tries to embed a Google map of the coordinates, but it isn't working ;(
#     """

#     search_url = "https://api.what3words.com/v3/convert-to-coordinates?key=" + "AFRG9VHR"

#     parameters = { "words":words,
#               }


#     coordinateString = ""
#     response = requests.get(search_url, params=parameters)         # request the page
#     data = response.json()
#     coordinateString += str(data["coordinates"]['lng'])
#     coordinateString += " , "
#     coordinateString += str(data["coordinates"]['lat'])
    
#     if response.status_code == 404:                 # page not found
#         print("For the words", words, "There was a problem with getting the page")
#         print(search_url)
#     return coordinateString



# if True:
#     words = ["varieties.gift.verdict",
#             "entrepreneur.farmland.chains",
#             "strategist.chroniclers.worryingly",
#             "juniors.bids.ladder",
#             "winners.splice.order"]
#     coordinates = {}
#     i =0
#     while i < len(words):
#         coordinates[words[i]] = convert_to_coordinates(words[i])
#         i+=1
#     print(coordinates)

    
