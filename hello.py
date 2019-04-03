import re
text = """Giraffes have aroused 
the curiosity of __ 
since earliest times. The 
giraffe is the tallest of all 
living __, but 
scientists are unable to 
explain how it got its long 
__. The 
giraffe's tremendous height,
which might reach __ , comes from it legs and __."""

def mad_libs(mls):
    hints = re.findall("_.*?_",mls)

    if hints is not None:
        for word in hints:
            q="Enter a word: {}".format(word)
            new=input(q)
            mls=mls.replace(word,new,1)
            print("\n")
            mls=mls.replace("\n","")
            print(mls)
    else:
        print("invalid mls")


mad_libs(text)
