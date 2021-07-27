"""
This script parses multiple test scripts in a folder.
It looks for the cdp neighbors and builds a graphviz
diagram to build a network topology.
"""


import glob
from graphviz import Source, Graph


def parse_indexer(start, end, data):
    """
    Function to find begin and end index so a more direct
    parsing can occur.

    start = start string
    end = end string
    data = iterable to parse

    To do: Catch errors.
    """
    indexer = -1
    for line in data:
        indexer += 1
        if start in line:
            index_start = indexer
            #print(f"Found start string: {line}")
        elif end in line:
            index_end = indexer
            #print(f"found end string: {line}")
    return index_start, index_end


"Create a variable that will contain a list of device, neighbor tuples."
graph_neighbors = []


"""
Read file(s) that contain SCRIPT.txt in the name.
*** ACTION: Adjust based on filename structure. ***
"""
for file_name in glob.glob("NRFK*"):
    "*** ACTION: Adjust the device variable to find the hostname based on filename structure. ***"
    device = file_name.split()[0]
    neighbors = []
    print(f"Current file being worked on: {file_name}")

    """
    Open file, read, and delete extra newlines.
    Create indexer variable to track begin and end markers.
    Perform narrower search for neighbors.
    """
    with open(file_name, "r") as f:
        output = f.read()
        output = output.splitlines()

        """
        Loop through each line, if start marker is found, grab the line index number.
        If end marker is found, grab the line index number.
        *** ACTION: Change start and end string as needed. ***
        """
        start_string = "show cdp neighbors detail"
        end_string = "Total cdp entries displayed"
        cdp_start, cdp_end = parse_indexer(start_string, end_string, output)

        """
        Loop through each line between begin and end markers from previous step.
        If domain name is found, add hostname to the neighbor list.
        *** ACTION: Adjust based on hostname structure. ***
        """
        for item in output[cdp_start:cdp_end]:
            if "NMCI-ISF.com" in item:
                neighbors.append(item.split()[2].rstrip("NMCI-ISF.com"))

        """
        Loop through each neighbor found, and create a new tuple
        (host device, neighbor) and add it to the graph neighbor list.
        """
        for neighbor in neighbors:
            graph_neighbors.append((device, neighbor))
        # print(graph_neighbors)
        # print("-" * 20)

        """
        Test to make sure the tuple can be unpacked.
        for neighbor in graph_neighbors:
            node1, node2 = neighbor
            print(node1, node2)
        """

print("File processing complete. See graphviz script below:\n")

"Create a strict graph, no redundant lines."
my_graph = Graph(strict=True)

"Configure nodes and edges."
for neighbor in graph_neighbors:
    node1, node2 = neighbor
    my_graph.edge(node1, node2)

source = my_graph.source


" To make customizations to the graph, update new_text."
original_text = "strict graph {"
new_text = "strict graph {\n{rank=same R1 R2 R3}\n{rank=min MGMT_SW}"
new_source = source.replace(original_text, new_text)

new_graph = Source(new_source)

"Output the data that can be pasted manually into graphviz."
print(new_graph)

"Un-comment and rename below if you want the script to generate the graph automatically."
# new_graph.render("My very first graphviz.gv")
