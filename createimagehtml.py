with open("wildlifeImages.txt") as f:
    for line in f:
        print("""<div class="12u"><span class="image fit"><img src="images/pics/wildlife/""" + line + """" alt="" /></span></div>""")