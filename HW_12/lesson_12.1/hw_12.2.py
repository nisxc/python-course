import xml.etree.cElementTree as ET


class XMLHelper:
    def add_tag(self, parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements


root = ET.Element('shop')
category = ET.SubElement(root, 'category', {'name': 'Vegan products'})
product_1 = ET.SubElement(category, 'product', {'name': 'Almond milk'})
product_2 = ET.SubElement(category, 'product', {'name': 'Another almond milk'})

ET.dump(root)

helper = XMLHelper()
helper.add_tag(product_1, {'type': 'cereals', 'price': '30$'})
helper.add_tag(product_2, {'type': 'pasta', 'price': '25$'})

tree = ET.ElementTree(root)
tree.write('vegan.xml', 'UTF-8', True)
