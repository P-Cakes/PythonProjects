from bs4 import BeautifulSoup
# IF we're using XML , install + import "lxml"
# Then change soup parser to xml

# if you get a decode error, try adding the encoding
# This error was caused by the heart emoji in the file
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# the contents is the markup (the M from HTML)
# Now we need to specify the parser for the langauge we are using
soup = BeautifulSoup(contents, "html.parser")

#print(soup.title)
#
# all_anchor_tags = soup.find_all(name ="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

#print (all_anchor_tags)

heading = soup.find(name="h1", id="name")
print (heading)

# Class keyword is reserved in Python so we use class_
section_heading = soup.find(name="h3", class_="heading")
print (section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)