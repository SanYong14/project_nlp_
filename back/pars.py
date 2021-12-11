import requests
# from . import tb
import xml.etree.ElementTree as ET
tree = ET.parse("G:\pythonshit\hackathon21_nlp\dataset_utf8 (2).xml")
root = tree.getroot()

print(root.tag)
for child in root:
    print(child.tag)
    if child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Worksheet":
        for step_child in child:
            print(step_child.tag)
            if step_child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Table":
                for step_step_child in step_child:
                    print(step_step_child.tag)
                    if step_step_child.tag == "{urn:schemas-microsoft-com:office:spreadsheet}Row":
                        for cell in step_step_child:
                            print(cell[0].text)
                            # print(cell[4].atrib)



# for event, elem in ET.iterparse("G:\pythonshit\hackathon21_nlp\dataset_utf8 (2).xml"):
#     print(elem)
