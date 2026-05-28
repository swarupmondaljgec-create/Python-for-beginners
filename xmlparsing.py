import xml.dom.minidom
doc = xml.dom.minidom.parse("sample.xml")
print(doc.nodeName)
print(doc.firstChild.nodeName)

for product in doc.getElementsByTagName("product"):
    if product.getAttribute("id") == "102":
        name_node = product.getElementsByTagName("name")[0]
        print(name_node.firstChild.nodeValue)
        break
