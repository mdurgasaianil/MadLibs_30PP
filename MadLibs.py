def get_input(strinput):
    user_input = input(f"Enter a {strinput}")
    return user_input

noun1 = get_input("noun: ")
verb1 = get_input("verb: ")
noun2 = get_input("noun: ")
verb2 = get_input("verb: ")

story = f"""
once upon a time, there was a {noun1} who loved to {verb1} all day.

One day, {noun2} walked into the room and caught the {noun1} in the act,

{noun2}: "what are you doing?"
{noun1}: "I'm just {verb1}ing, what's the big deal?"
{noun2}: "Well, it's not every that you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "That's probably a good idea. why don't we go {verb2} instead?"

And so, {noun2} and the {noun1} went off to {verb2} and had a great time.

----- The End -----
"""

print(story)