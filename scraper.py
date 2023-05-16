from bs4 import BeautifulSoup
import requests as req
url='https://codewithharry.com'

#step 0- install requirements done
#step 1: get html
#step 2: parse html
#step 3: html tree traverse
page=req.get(url)
htmlContent = page.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())
# step 2 done
# step 3:
title=soup.title
# print(title)
#commonly used types of objects
#tags, navigable strings, beautifulsoup,comments -> navigable strings are diff from regular strings
# print(type(title))
# print(type(soup))
# print(type(title.string))

# get all paragraphs

pg=soup.find_all('p')
# print(pg)

anchors=soup.find_all('a')
# print(anchors)
# print('\n\n\n')
# print(soup.find('p')['class'])
# find all the elements with class lead
# print(soup.find_all('p',class_='lead'))

# get text from elements:
# print(soup.get_text())

all_links =set()
for link in anchors:
    if(link.get('href')=='#'):
        linker="https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linker)
# print(all_links)

markup="<p><!-- this is a comment --></p>"
soup2=BeautifulSoup(markup,features='lxml')
# print(soup2.p)

next=soup.find(id='__next')
# print(next)
print(next.children)
# print(next.contents)
# for elements in next.strings:
# print(elements.parent)
# print(next.parent)
# for item in next.strings:
    # print(item.name)

# print(next.next_sibling.next_sibling)
elem=soup.select('.shadow-md')
for i in elem:
    print(i.stripped_strings)
    print(i.strings)