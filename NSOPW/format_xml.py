import clipboard
import xml.dom.minidom

xml = xml.dom.minidom.parse('./result.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()

clipboard.set(pretty_xml_as_string)
