import xml.etree.cElementTree as ET

# tree = ET.parse("books.xml")
# root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

# for book in root.findall('book'):
#     print(book.get('title'))

# for child in root:
#     child.tag = 'g'
#     child.remove(child.find('author'))
#     child.set('data', "5")
#     print(child.tag, child.attrib)
# tree.write('movie.xml', 'UTF-8', True)
# print(root.find('g').get('title'))

root = ET.Element('data')
mov1 = ET.SubElement(root, 'movie', {'title': 'Hello '})
mov2 = ET.SubElement(root, 'movie', {'title': 'Hello 2 '})
ET.dump(root)
print(root)
