# /////////////////////////////////////////////////////////////////////////////////////////////
# Don't Consider

import xml.etree.ElementTree as ET

def create_routes_file():
    # Create the root element
    root = ET.Element("routes")

    # Add the first route
    route1 = ET.SubElement(root, "route", id="route1", edges="150785556#0 150785556#0-AddedOffRampEdge", departProbability="0.1")

    # Add the second route
    route2 = ET.SubElement(root, "route", id="route2", edges="36913434 1110191850", departProbability="0.9")

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Save the XML tree to a file
    tree.write("od_matrix.xml")

if __name__ == "__main__":
    create_routes_file()

# OD_MATRIX FILE INITIAL
# <routes><route id="route1" edges="edge1 edge2" departProbability="0.1" /><route id="route2" edges="edge3 edge4" departProbability="0.9" /></routes>
