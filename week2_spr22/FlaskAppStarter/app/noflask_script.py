# 
# if flask simply won't work, this is a less-exciting "substitute"!
#

import pythonfunctions   # for the substitute function

#
# you'll implement the substitute function not here, but in pythonfunctions.py
#
#    then, you'll text it here:
#

if True:
    # here is the default example from the flask website:
    # 
    old_text = "Our candidate insists on a global solution to this pressing problem." 
    
    old_word1 = "candidate"
    old_word2 = "global"
    old_word3 = "pressing"

    new_word1 = "airbender"
    new_word2 = "spherical"
    new_word3 = "calculus"

    # create a dictionary of substitutions
    substitutions = {}
    substitutions[old_word1] = new_word1
    substitutions[old_word2] = new_word2
    substitutions[old_word3] = new_word3

    # call substitute!
    new_text = pythonfunctions.substitute(old_text, substitutions)

    # print the results
    print("\n")
    print("old_text was\n\n", old_text)
    print("\n")
    print("new_text is\n\n", new_text)
    print("\n")

    #  return new_text    # not really needed here...

    # here is my example:
    # 
    old_text = "Our candidate insists on a global solution to this pressing problem." 
    
    old_word1 = "candidate"
    old_word2 = "global"
    old_word3 = "pressing"

    new_word1 = "professor"
    new_word2 = "another"
    new_word3 = "substitution"

    # create a dictionary of substitutions
    substitutions = {}
    substitutions[old_word1] = new_word1
    substitutions[old_word2] = new_word2
    substitutions[old_word3] = new_word3

    # call substitute!
    new_text = pythonfunctions.substitute(old_text, substitutions)

    # print the results
    print("\n")
    print("old_text was\n\n", old_text)
    print("\n")
    print("new_text is\n\n", new_text)
    print("\n")


    # here is my example:
    # 
    old_text = "The king doth wake tonight and takes his rouse." 
    
    old_word1 = "doth"
    old_word2 = "rouse"
    

    new_word1 = '<span style="color:rgb(0, 0, 150);" title="doth"> does </span>'
    new_word2 = '<span style="color:rgb(0, 0, 150);" title="rouse"> party </span>'
    

    # create a dictionary of substitutions
    substitutions = {}
    substitutions[old_word1] = new_word1
    substitutions[old_word2] = new_word2
    

    # call substitute!
    new_text = pythonfunctions.substitute(old_text, substitutions)

    # print the results
    print("\n")
    print("old_text was\n\n", old_text)
    print("\n")
    print("new_text is\n\n", new_text)
    print("\n")


