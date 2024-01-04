import xml.etree.ElementTree as ET

def create_taz_file(od_matrix_file, taz_file):
    print("1")
    # Parse the OD matrix XML file
    tree = ET.parse(od_matrix_file)
    print("2")
    root = tree.getroot()
    print("3")

    # Extract unique zones from the OD matrix
    unique_zones = set()
    print("4")
    for trip in root.findall(".//trip"):
        unique_zones.add(trip.get("from"))
        unique_zones.add(trip.get("to"))
    print("5")
    # Create the root element for the TAZ file
    root_taz = ET.Element("tazs")
    print("6")
    # Add TAZ elements based on unique zones
    for zone in unique_zones:
        taz = ET.SubElement(root_taz, "taz", id=str(zone))
        ET.SubElement(taz, "name").text = f"TAZ_{zone}"
        ET.SubElement(taz, "population").text = str(1000)  # You can replace this with actual population data
        ET.SubElement(taz, "area").text = str(50)  # You can replace this with actual area data
    print("7")
    # Create the XML tree for the TAZ file
    tree_taz = ET.ElementTree(root_taz)
    print("8")
    # Save the XML tree to the output file
    tree_taz.write(taz_file)
    print("9")

if __name__ == "__main__":
    od_matrix_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_matrix.xml"  # Replace with the path to your OD matrix file in XML format
    taz_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\taz_file.xml"
    create_taz_file(od_matrix_file, taz_file)
    print("0")
    print(f"TAZ file '{taz_file}' created successfully.")





# import xml.etree.ElementTree as ET
# import pandas as pd

# def create_taz_file(od_matrix_file, taz_file):
#     # Read the OD matrix data from a CSV file (you may need to adjust this based on your file format)
#     od_matrix_data = ET.parse(od_matrix_file)
#     # root = tree.getroot()

#     # Extract unique zones from the OD matrix
#     unique_zones = set(od_matrix_data['origin']).union(set(od_matrix_data['destination']))

#     # Create the root element
#     root = ET.Element("tazs")

#     # Add TAZ elements based on unique zones
#     for zone in unique_zones:
#         taz = ET.SubElement(root, "taz", id=str(zone))
#         ET.SubElement(taz, "name").text = f"TAZ_{zone}"
#         ET.SubElement(taz, "population").text = str(1000)  # You can replace this with actual population data
#         ET.SubElement(taz, "area").text = str(50)  # You can replace this with actual area data

#     # Create the XML tree
#     tree = ET.ElementTree(root)

#     # Save the XML tree to the output file
#     tree.write(taz_file)

# if __name__ == "__main__":
#     od_matrix_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_matrix.xml"  # Replace with the path to your OD matrix file
#     taz_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\taz_file.xml"
#     create_taz_file(od_matrix_file, taz_file)
#     print(f"TAZ file '{taz_file}' created successfully.")
