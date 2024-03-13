import xml.dom.minidom as xmldom


if __name__ == "__main__":
    # 加载 XML 文件
    xml_file = xmldom.parse('3.xml')
    tracks = xml_file.getElementsByTagName('track')

    # 遍历所有的标注对象
    for track in tracks:
        label = track.getAttribute('label')
        if label == 'cotton_ball':
            track.setAttribute('label', 'gauze')

    # 将修改后的 XML 文件保存
    with open('modified_annotations.xml', 'w') as f:
        xml_file.writexml(f)
