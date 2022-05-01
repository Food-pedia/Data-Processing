from xml.etree.ElementTree import Element, SubElement, ElementTree
import os
import shutil

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


with open('crop_area.properties', 'r', encoding="utf-8") as file:
    label = 'food'
    os.mkdir(label)
    for text in file:
        try:
            filename = text.split('=')[0]
            xmin = text.split('=')[1].split(',')[0]
            xmax = text.split('=')[1].split(',')[1].split(',')[0]
            ymin = text.split('=')[1].split(',')[2].split(',')[0]
            ymax = text.split('=')[1].split(',')[3].split(',')[0]

            width = 640
            height = 640

            root = Element('annotation')
            SubElement(root, 'folder')
            SubElement(root, 'filename').text = filename + '.jpg'
            SubElement(root, 'path').text = filename + '.jpg'
            source = SubElement(root, 'source')
            SubElement(source, 'database').text = 'Unknown'

            size = SubElement(root, 'size')
            SubElement(size, 'width').text = str(width)
            SubElement(size, 'height').text = str(height)
            SubElement(size, 'depth').text = '3'

            SubElement(root, 'segmented').text = '0'

            obj = SubElement(root, 'object')
            SubElement(obj, 'name').text = label
            SubElement(obj, 'pose').text = 'Unspecified'
            SubElement(obj, 'truncated').text = '0'
            SubElement(obj, 'difficult').text = '0'
            SubElement(obj, 'occluded').text = '0'
            bbox = SubElement(obj, 'bndbox')
            SubElement(bbox, 'xmin').text = xmin
            SubElement(bbox, 'ymin').text = xmax
            SubElement(bbox, 'xmax').text = ymin
            SubElement(bbox, 'ymax').text = ymax

            indent(root)

            tree = ElementTree(root)
            tree.write('./'+label+'/' + filename + '.xml', encoding='utf8')
        except IndexError:
            continue
