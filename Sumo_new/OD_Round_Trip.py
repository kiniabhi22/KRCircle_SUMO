# # Set the SUMO_HOME environment variable to the directory containing "sumo" binary
# print("1")
# if 'SUMO_HOME' in os.environ:
#     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
#     sys.path.append(tools)
# else:
#     sys.exit("Please set the SUMO_HOME environment variable")

# # Set the path to your SUMO binary
# print("2")
# sumo_binary = checkBinary('sumo')
# sumocmd=["C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui", "-c", "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_Round_Trip.sumocfg"]
# # Path to your network file (.net.xml)
# # network_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\osm.net.xml"

# # Path to your OD matrix file
# od_matrix_file = "C:\\Users\\HP\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_matrix.xml"

# # Path to output trips file
# output_trips_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\output_dynamic_routes.rou.xml"

# # Path to your SUMO configuration file
# sumo_config_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_Round_Trip.sumocfg"
# # sumo_binary=r"C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui"

# print("3")
# def generate_routes():
#     print("4")
#     # Initialize SUMO simulation
#     traci.start(sumocmd)
#     print("5")
#     # Load the OD matrix
#     traci.route.addFile(od_matrix_file)
#     print("6")
#     # Generate routes using the OD matrix
#     traci.simulationStep()
#     print("7")
#     # Save the generated routes to a file
#     traci.route.save(output_trips_file)
#     print("8")
#     # Close the SUMO simulation
#     traci.close()

# if __name__ == "__main__":
#     print("0")
#     generate_routes()

import os
import subprocess

def generate_trips(od_matrix_file, taz_file, output_trips_file, sumo_tools_path):
    od2trips_cmd = os.path.join(sumo_tools_path, "od2trips")

    # Run od2trips tool to generate trips file
    subprocess.run([od2trips_cmd, "--d",od_matrix_file, "--taz-files",taz_file, "--output-file",output_trips_file])



if __name__ == "__main__":
    # Replace these paths with your actual file paths and SUMO tools path
    od_matrix_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\od_matrix.xml"
    taz_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\taz_file.xml"
    output_trips_file = "C:\\Users\\HP\\Sumo\\Sumo-KRCircle-File-main\\venv\\SUMO_VENV\\result.xml" 
    sumo_tools_path = "C:\\Program Files (x86)\\Eclipse\\Sumo\\tools"

    generate_trips(od_matrix_file, taz_file, output_trips_file, sumo_tools_path)
