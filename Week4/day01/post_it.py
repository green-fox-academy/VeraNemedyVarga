"""Create a PostIt class that has
a backgroundColor
a text on it
a textColor
Create a few example post-it objects:
an orange with blue text: "Idea 1"
a pink with black text: "Awesome"
a yellow with green text: "Superb!"
"""
class PostIt():
    backgroundColor = ''
    text = ''
    textColor = ''

post_it1 = PostIt()
post_it1.backgroundColor = "orange"
post_it1.text = "Idea1"
post_it1.textColor = "blue"
print(post_it1.backgroundColor + " " + post_it1.text + " " + post_it1.textColor)

post_it2 = PostIt()
post_it2.backgroundColor = "pink"
post_it2.text = "Awesome"
post_it2.textColor = "black"

post_it3 = PostIt()
post_it3.backgroundColor = "yellow"
post_it3.text = "Superb!"
post_it3.textColor = "green"
