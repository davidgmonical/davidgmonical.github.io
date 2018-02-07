import os
for filename in os.listdir("images/thumbs/other/"):
	if filename.endswith(".jpg") or filename.endswith(".png"): 
		print("""<div class="4u"><span class="image fit"><img src="images/thumbs/other/""" + filename + """" alt="" /></span></div>""")

        