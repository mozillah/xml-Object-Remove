import os, os.path, sys
import glob
from os.path import join
import argparse
from xml.etree import ElementTree
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element

parser = argparse.ArgumentParser(description='xmls Merge')
parser.add_argument('--folder', help='Path to video file.')
args = parser.parse_args()


folderpath= ""
secondfolder = "WithoutGender"
output_folder= join(args.folder, 'newumarfishtest')
if (args.folder):
    folderpath= args.folder
else:
    exit(1)

    
xml_files= glob.glob(folderpath +"/*.xml")
output_folder= join(os.path.normpath(folderpath + os.sep + os.pardir), secondfolder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for file in xml_files:
    base=os.path.basename(file)
    print(base)
    searchfile = os.path.join(output_folder, base)
    print(f"Outputfile== {searchfile}")
    print(f"Originalfile== {file}")
    # print(file)
    data1 = ElementTree.parse(file).getroot()
    Objects=data1.findall("./object")
    print(len(Objects))
    for elem in Objects:
        print(elem.find("name").text)
        if (elem.find("name").text == "Male" or elem.find("name").text == "Female") :
            data1.remove(elem)
    tree = ET.ElementTree(data1)
    tree.write(searchfile, encoding="utf-8")