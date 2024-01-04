import xml.etree.ElementTree as ET

def create_sumocfg_file(net_file, route_files, begin_time, end_time, output_file="od_Round_Trip.sumocfg.xml"):
    # Create the root element
    root = ET.Element("configuration")

    # Add the input section
    input_element = ET.SubElement(root, "input")
    ET.SubElement(input_element, "net-file", value=net_file)
    ET.SubElement(input_element, "route-files", value=route_files)

    # Add the time section
    time_element = ET.SubElement(root, "time")
    ET.SubElement(time_element, "begin", value=str(begin_time))
    ET.SubElement(time_element, "end", value=str(end_time))

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Save the XML tree to a file
    tree.write(output_file)

if __name__ == "__main__":
    # Example usage
    create_sumocfg_file(
        net_file="C:\\Users\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\osm.net.xml",
        route_files="C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\output_dynamic_routes.rou.xml",
        begin_time=0,
        end_time=3600
    )
