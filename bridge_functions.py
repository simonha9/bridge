""" 
Assignment 2: Bridges

The data used for this assignment is a subset of the data found in:
https://www.ontario.ca/data/bridge-conditions
"""

import csv
import math
from typing import List, TextIO

ID_INDEX = 0
NAME_INDEX = 1
HIGHWAY_INDEX = 2
LAT_INDEX = 3
LON_INDEX = 4
YEAR_INDEX = 5
LAST_MAJOR_INDEX = 6
LAST_MINOR_INDEX = 7
NUM_SPANS_INDEX = 8
SPAN_LENGTH_INDEX = 9
LENGTH_INDEX = 10
LAST_INSPECTED_INDEX = 11
BCIS_INDEX = 12
NUM_COLS_FORMATTED = 13
INSP_LAT_INDEX = 0
INSP_LON_INDEX = 1

HIGH_PRIORITY_BCI = 60   
MEDIUM_PRIORITY_BCI = 70
LOW_PRIORITY_BCI = 100

HIGH_PRIORITY_RADIUS = 500  
MEDIUM_PRIORITY_RADIUS = 250
LOW_PRIORITY_RADIUS = 100

EARTH_RADIUS = 6371

####### BEGIN HELPER FUNCTIONS ####################

def read_data(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on csv_file.
    """ 

    lines = csv.reader(csv_file)
    data = list(lines)[2:]
    return data


def calculate_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Return the distance in kilometers between the two locations defined by   
    (lat1, lon1) and (lat2, lon2), rounded to the nearest meter.
    
    >>> calculate_distance(43.659777, -79.397383, 43.657129, -79.399439)
    0.338
    >>> calculate_distance(43.42, -79.24, 53.32, -113.30)
    2713.226
    """

    # This function uses the haversine function to find the
    # distance between two locations. You do NOT need to understand why it
    # works. You will just need to call on the function and work with what it
    # returns.
    # Based on code at goo.gl/JrPG4j

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = (math.radians(lon1), math.radians(lat1), 
                              math.radians(lon2), math.radians(lat2))

    # haversine formula t
    lon_diff = lon2 - lon1 
    lat_diff = lat2 - lat1 
    a = (math.sin(lat_diff / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin(lon_diff / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return round(c * EARTH_RADIUS, 3)


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

THREE_BRIDGES_UNCLEANED = [
    ['1 -  32/', 'Highway 24 Underpass at Highway 403', '403', '43.167233',
     '-80.275567', '1965', '2014', '2009', '4',
     'Total=64  (1)=12;(2)=19;(3)=21;(4)=12;', '65', '04/13/2012', '72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     ''],
    ['1 -  43/', 'WEST STREET UNDERPASS', '403', '43.164531', '-80.251582',
     '1963', '2014', '2007', '4',
     'Total=60.4  (1)=12.2;(2)=18;(3)=18;(4)=12.2;', '61', '04/13/2012',
     '71.5', '', '71.5', '', '68.1', '', '69', '', '69.4', '', '69.4', '',
     '70.3', '73.3', ''],
    ['2 -   4/', 'STOKES RIVER BRIDGE', '6', '45.036739', '-81.33579', '1958',
     '2013', '', '1', 'Total=16  (1)=16;', '18.4', '08/28/2013', '85.1',
     '85.1', '', '67.8', '', '67.4', '', '69.2', '70', '70.5', '', '75.1', '',
     '90.1', '']
    ]

THREE_BRIDGES = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,
                  -80.275567, '1965', '2014', '2009', 4,
                  [12.0, 19.0, 21.0, 12.0], 65.0, '04/13/2012',
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]],
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582,
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, 
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,
                                 73.3]],
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958',
                  '2013', '', 1, [16.0], 18.4, '08/28/2013',
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]
                ]

#################################################
def format_data(data: List[List[str]]) -> None:  
    """Modify data so that it follows the format outlined in the 
    'Data formatting' section of the assignment handout.
    
    >>> d = THREE_BRIDGES_UNCLEANED
    >>> format_data(d)
    >>> d == THREE_BRIDGES
    True
    """
    
    for i in range(len(data)):           
        formatted_bridge_data = [None] * NUM_COLS_FORMATTED
        formatted_bridge_data[ID_INDEX] = (i + 1) #id
        formatted_bridge_data[NAME_INDEX] = (data[i][NAME_INDEX]) #name
        formatted_bridge_data[HIGHWAY_INDEX] = (data[i][HIGHWAY_INDEX]) #highway
        
        latitude = 0.0
        if len(data[i][LAT_INDEX]) > 0:
            latitude = float(data[i][LAT_INDEX])
        formatted_bridge_data[LAT_INDEX] = latitude #latitude
        
        longitude = 0.0
        if len(data[i][LON_INDEX]) > 0:
            longitude = float(data[i][LON_INDEX])
        formatted_bridge_data[LON_INDEX] = longitude #longitude
        
        formatted_bridge_data[YEAR_INDEX] = (data[i][YEAR_INDEX]) #year built
        formatted_bridge_data[LAST_MAJOR_INDEX] = \
            (data[i][LAST_MAJOR_INDEX]) # major rehab
        formatted_bridge_data[LAST_MINOR_INDEX] = \
            (data[i][LAST_MINOR_INDEX]) #minor rehab
        formatted_bridge_data[NUM_SPANS_INDEX] = \
            (int(data[i][NUM_SPANS_INDEX])) #number of spans
        formatted_bridge_data[SPAN_LENGTH_INDEX] = \
            format_span_details(data[i][SPAN_LENGTH_INDEX]) #span details
        
        length = 0.0
        if len(data[i][LENGTH_INDEX]) > 0:
            length = float(data[i][LENGTH_INDEX])
        formatted_bridge_data[LENGTH_INDEX] = length #bridge length
        
        formatted_bridge_data[LAST_INSPECTED_INDEX] = \
            (data[i][LAST_INSPECTED_INDEX]) #last inspected date
        formatted_bridge_data[BCIS_INDEX] = \
            format_bridge_bcis(data[i][BCIS_INDEX:]) #BCIs
        data[i] = formatted_bridge_data
        

    
def format_span_details(span_details_uncleaned: str) -> List[str]:
    """Formats span_details_uncleaned into a formatted version of the 
    span details
    
    Precondition: span_details_uncleaned is in the format:
    'total<total_length> (1)=<span_length1>;(2)=<span_length2> ...'
    
    >>>format_span_details('Total=64  (1)=12;(2)=19;(3)=21;(4)=12;')
    [12.0, 19.0, 21.0, 12.0]
    """
    formatted_span_details = []
    span_details = span_details_uncleaned.split(";")
    for span in span_details:
        for span_num_len in span.split("=")[1:]:
            if not span_num_len.endswith(")"):
                formatted_span_details.append(float(span_num_len))
    return formatted_span_details

def format_bridge_bcis(bridge_bcis_uncleaned: List[str]) -> List[float]:
    """Formats bridge_bcis_uncleaned and returns a formatted list of 
    bridge bcis
    
    >>>format_bridge_bcis('72.3', '',
     '72.3', '', '69.5', '', '70', '', '70.3', '', '70.5', '', '70.7', '72.9',
     '')
     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]
    """
    bridge_bcis = []
    for item in bridge_bcis_uncleaned:
        if len(item) > 0:
            bridge_bcis.append(float(item))
    if len(bridge_bcis) > 0 and bridge_bcis[0] == bridge_bcis[1]:
        bridge_bcis.remove(bridge_bcis[1])
    return bridge_bcis
 
def get_bridge(bridge_data: List[list], bridge_id: int) -> list:
    """Return the data for the bridge with id bridge_id from bridge_data. If
    there is no bridge with the given id, return an empty list.  
    
    >>> result = get_bridge(THREE_BRIDGES, 1)
    >>> result == [1, 'Highway 24 Underpass at Highway 403', '403', 43.167233, \
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]]
    True
    """
    
    for bridge in bridge_data:
        if bridge[ID_INDEX] == bridge_id:
            return bridge
    return []


def get_average_bci(bridge_data: List[list], bridge_id: int) -> float:
    """Return the average BCI for the bridge with bridge_id from bridge_data.
    If there is no bridge with the id bridge_id, return 0.0. If there are no
    BCIs for the bridge with id bridge_id, return 0.0.
    
    >>> get_average_bci(THREE_BRIDGES, 1)   
    70.88571428571429
    """
    
    average = 0.0
    total_bci = 0.0
    bridge = get_bridge(bridge_data, bridge_id)
    
    if len(bridge) > 0:
        for bridge_bci in bridge[BCIS_INDEX]:
            total_bci = total_bci + bridge_bci
        average = total_bci/len(bridge[BCIS_INDEX]) 

    return average   


def get_total_length_on_highway(bridge_data: List[list], highway: str) -> float:
    """Return the total length of bridges in bridge_data on highway.
    Use zero for the length of bridges that do not have a length provided.
    If there are no bridges on highway, return 0.0.
    
    >>> get_total_length_on_highway(THREE_BRIDGES, '403')
    126.0
    >>> get_total_length_on_highway(THREE_BRIDGES, '401')
    0.0
    """
    
    total_length = 0.0
    for bridge in get_bridges_on_highway(bridge_data, highway):
        if len(bridge) > 0:
            total_length = total_length + bridge[LENGTH_INDEX]           
    return total_length

def get_bridges_on_highway(bridge_data: List[list], highway: str) -> List[int]:
    """Returns a list of bridges that are on highway from bridge_data
    
    >>>result = get_bridges_on_highway(THREE_BRIDGES, '403')
    >>>result == [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
    -80.275567, '1965', '2014', '2009', 4, [12.0, 19.0, 21.0, 12.0], 65.0, \
    '04/13/2012', [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, '1963', '2014',\
    '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, '04/13/2012', \
    [71.5, 68.1, 69.0, 69.4, 69.4, 70.3, 73.3]]]
    True
    """
    bridges_on_highway = []
    for bridge in bridge_data:
        if highway == bridge[HIGHWAY_INDEX]:
            bridges_on_highway.append(bridge)
    return bridges_on_highway

def get_distance_between(bridge1: list, bridge2: list) -> float:
    """Return the distance in kilometres, rounded to the nearest metre
    (i.e., 3 decimal places), between the two bridges bridge1 and bridge2.
        
    >>> get_distance_between(get_bridge(THREE_BRIDGES, 1), \
                                 get_bridge(THREE_BRIDGES, 2))
    1.968
    """
    
    return calculate_distance(bridge1[LAT_INDEX], bridge1[LON_INDEX], \
                              bridge2[LAT_INDEX], bridge2[LON_INDEX])
    
    
def find_closest_bridge(bridge_data: List[list], bridge_id: int) -> int:
    """Return the id of the bridge in bridge_data that has the shortest
    distance to the bridge with id bridge_id.
    
    Precondition: a bridge with bridge_id is in bridge_data, and there are
    at least two bridges in bridge_data
    
    >>> find_closest_bridge(THREE_BRIDGES, 2)
    1
    """
    initial_bridge = bridge_data[0]
    bridge_reference = get_bridge(bridge_data, bridge_id)
    bridge_ref_lat = bridge_reference[LAT_INDEX]
    bridge_ref_lon = bridge_reference[LON_INDEX]
    shortest_dist = get_distance_between(initial_bridge, bridge_reference)
    shortest_dist_bridge_id = initial_bridge[ID_INDEX]
    
    for bridge in bridge_data[1:]:
        if bridge[ID_INDEX] != bridge_id:
            dist = calculate_distance(bridge[LAT_INDEX], \
                                      bridge[LON_INDEX], 
                                      bridge_ref_lat, bridge_ref_lon)            
            if shortest_dist > dist:
                shortest_dist = dist
                shortest_dist_bridge_id = bridge[ID_INDEX]
        
    return shortest_dist_bridge_id


def find_bridges_in_radius(bridge_data: List[list], lat: float, long: float,
                           distance: float) -> List[int]:
    """Return the IDs of the bridges that are within radius distance
    from (lat, long).
    
    >>> find_bridges_in_radius(THREE_BRIDGES, 43.10, -80.15, 50)
    [1, 2]
    """
    bridges_in_radius = []
    
    for bridge in bridge_data:
        bridge_distance = calculate_distance(bridge[LAT_INDEX], \
                                             bridge[LON_INDEX], lat, long)
        if bridge_distance <= distance:
            bridges_in_radius.append(bridge[ID_INDEX])
    return bridges_in_radius


def get_bridges_with_bci_below(bridge_data: List[list], bridge_ids: List[int],
                               bci_limit: float) -> List[int]:
    """Return the IDs of the bridges with ids in bridge_ids whose most
    recent BCIs are less than or equal to bci_limit.
    
    >>> get_bridges_with_bci_below(THREE_BRIDGES, [1, 2], 72)
    [2]
    """
    result = []
    for bridge_id in bridge_ids:
        bridge = get_bridge(bridge_data, bridge_id)
        if len(bridge) > 0 and bridge[BCIS_INDEX][0] <= bci_limit:
            result.append(bridge_id)      
    return result


def get_bridges_containing(bridge_data: List[list], search: str) -> List[int]:
    """
    Return a list of IDs of bridges whose names contain search (case
    insensitive).
    
    >>> get_bridges_containing(THREE_BRIDGES, 'underpass')
    [1, 2]
    >>> get_bridges_containing(THREE_BRIDGES, 'Highway')
    [1]
    """
    
    result = []
    for bridge in bridge_data:
        if search.lower() in bridge[NAME_INDEX].lower():
            result.append(bridge[ID_INDEX])
    return result


def assign_inspectors(bridge_data: List[list], inspectors: List[List[float]],
                      max_bridges: int) -> List[List[int]]:
    """Return a list of bridge IDs to be assigned to each inspector in
    inspectors. inspectors is a list containing (latitude, longitude) pairs
    representing each inspector's location.
    
    At most max_bridges bridges should be assigned to an inspector, and each
    bridge should only be assigned once (to the first inspector that can
    inspect that bridge).
    
    See the "Assigning Inspectors" section of the handout for more details.
    
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 1)
    [[1]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 2)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.10, -80.15]], 3)
    [[1, 2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 1)
    [[1], [2]]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [43.10, -80.15]], 2)
    [[1, 2], []]
    >>> assign_inspectors(THREE_BRIDGES, [[43.20, -80.35], [45.0368, -81.34]], 2)
    [[1, 2], [3]]
    >>> assign_inspectors(THREE_BRIDGES, [[38.691, -80.85], [43.20, -80.35]], 2)
    [[], [1, 2]]
    """
    
    result = []
    unassigned_bridges = bridge_data
    for inspector in inspectors:
        assigned_bridge_ids = []

        new_assigned_bridge_ids = assign_bridges_to_inspector(inspector, \
                                                  HIGH_PRIORITY_RADIUS, \
                                                  HIGH_PRIORITY_BCI, \
                                                  max_bridges, \
                                                  unassigned_bridges)
        unassigned_bridges = get_unassigned_bridges(unassigned_bridges, \
                                                    new_assigned_bridge_ids)        
        assigned_bridge_ids.extend(new_assigned_bridge_ids)
        if len(assigned_bridge_ids) < max_bridges:
            new_assigned_bridge_ids = assign_bridges_to_inspector(inspector, \
                                                      MEDIUM_PRIORITY_RADIUS, \
                                                      MEDIUM_PRIORITY_BCI, \
                                                      max_bridges - \
                                                      len(assigned_bridge_ids), \
                                                      unassigned_bridges)
            unassigned_bridges = get_unassigned_bridges(unassigned_bridges, \
                                                        new_assigned_bridge_ids)            
            assigned_bridge_ids.extend(new_assigned_bridge_ids)
        
        if len(assigned_bridge_ids) < max_bridges:
            new_assigned_bridge_ids = assign_bridges_to_inspector(inspector, \
                                                      LOW_PRIORITY_RADIUS, \
                                                      LOW_PRIORITY_BCI, \
                                                      max_bridges - \
                                                      len(assigned_bridge_ids), \
                                                      unassigned_bridges)
            unassigned_bridges = get_unassigned_bridges(unassigned_bridges, \
                                                        new_assigned_bridge_ids)
            assigned_bridge_ids.extend(new_assigned_bridge_ids)
        result.append(assigned_bridge_ids)
    return result

def assign_bridges_to_inspector(inspector: List[float], priority_radius: int, \
                               priority_bci: int, \
                               max_bridges: int, \
                               unassigned_bridges: List[list]) -> List[int]:                            
    """Returns a list of bridge ids less than max_bridges in unassigned_bridges
    for inspector given priority_radius and priority_bci.  
    
    >>>assign_bridges_to_inspector([43.10, -80.15], LOW_PRIORITY_RADIUS, \
    LOW_PRIORITY_BCI, 1, THREE_BRIDGES)
    [1]
    """
    
    #Gets bridges within priority_radius    
    bridges_within_radius = find_bridges_in_radius(unassigned_bridges,
                                                   inspector[INSP_LAT_INDEX], 
                                                   inspector[INSP_LON_INDEX],
                                                   priority_radius) 
    
    #Gets ids of bridges within priority_radius and below bci    
    bridge_ids_to_inspect = get_bridges_with_bci_below(unassigned_bridges, 
                                                       bridges_within_radius, 
                                                       priority_bci)
    
    #Sorts bridge ids in ascending order
    bridge_ids_to_inspect.sort()
    
    num_bridge_ids = min(max_bridges, len(bridge_ids_to_inspect))
    assigned_bridge_ids = bridge_ids_to_inspect[:num_bridge_ids]
    return assigned_bridge_ids
        
def get_unassigned_bridges(bridge_data: List[list], \
                           assigned_bridges: List[int]) -> List[list]:
    """Returns a list of bridges from bridge_data with the 
    assigned_bridges removed    
    
    >>>result = get_unassigned_bridges(THREE_BRIDGES, [1])
    >>>result == [[2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
    '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61.0, '04/13/2012', \
    [71.5, 68.1, 69.0, 69.4, 69.4, 70.3, 73.3]], [3, 'STOKES RIVER BRIDGE',\
    '6', 45.036739, -81.33579, '1958', '2013', '', 1, [16.0], 18.4, \
    '08/28/2013', [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]]]
    True
    """
    if len(assigned_bridges) == 0:
        return bridge_data
    unassigned_bridges = []
    for bridge in bridge_data:
        if bridge[ID_INDEX] not in assigned_bridges:
            unassigned_bridges.append(bridge)
    return unassigned_bridges

def inspect_bridges(bridge_data: List[list], bridge_ids: List[int], date: str, 
                    bci: float) -> None:
    """Update the bridges in bridge_data with id in bridge_ids with the new
    date and BCI score for a new inspection.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> inspect_bridges(bridges, [1], '09/15/2018', 71.9)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2009', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '09/15/2018', \
                     [71.9, 72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
    for bridge in bridge_data:
        if bridge[ID_INDEX] in bridge_ids:
            bridge[LAST_INSPECTED_INDEX] = date
            bridge[BCIS_INDEX].insert(0, bci)
    

def add_rehab(bridge_data: List[list], bridge_id: int, new_date: str, 
              is_major: bool) -> None:
    """
    Update the bridge with the id bridge_id to have its last rehab set to
    new_date. If is_major is True, update the major rehab date. Otherwise,
    update the minor rehab date.
    
    >>> bridges = [[1, 'Highway 24 Underpass at Highway 403', '403', 43.167233,\
                  -80.275567, '1965', '2014', '2009', 4, \
                  [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                  [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                 [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                  '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], 61, \
                  '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, 70.3,\
                                 73.3]], \
                 [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, '1958', \
                  '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                  [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                 ]
    >>> add_rehab(bridges, 1, '2018', False)
    >>> bridges == [[1, 'Highway 24 Underpass at Highway 403', '403', \
                     43.167233, -80.275567, '1965', '2014', '2018', 4, \
                     [12.0, 19.0, 21.0, 12.0], 65, '04/13/2012', \
                     [72.3, 69.5, 70.0, 70.3, 70.5, 70.7, 72.9]], \
                    [2, 'WEST STREET UNDERPASS', '403', 43.164531, -80.251582, \
                     '1963', '2014', '2007', 4, [12.2, 18.0, 18.0, 12.2], \
                     61, '04/13/2012', [71.5, 68.1, 69.0, 69.4, 69.4, \
                                          70.3, 73.3]], \
                    [3, 'STOKES RIVER BRIDGE', '6', 45.036739, -81.33579, \
                     '1958', '2013', '', 1, [16.0], 18.4, '08/28/2013', \
                     [85.1, 67.8, 67.4, 69.2, 70.0, 70.5, 75.1, 90.1]] \
                   ]
    True
    """
    bridge = get_bridge(bridge_data, bridge_id)
    if len(bridge) > 0:
        if is_major:
            bridge[LAST_MAJOR_INDEX] = new_date
        else:
            bridge[LAST_MINOR_INDEX] = new_date



if __name__ == '__main__':
    pass 

    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    # bridges = read_data(open('bridge_data.csv'))
    # format_data(bridges)

    # # For example,
    # print(get_bridge(bridges, 3))
    # expected = [3, 'NORTH PARK STEET UNDERPASS', '403', 43.165918, -80.263791,
    #             '1962', '2013', '2009', 4, [12.2, 18.0, 18.0, 12.2], 60.8,
    #             '04/13/2012', [71.4, 69.9, 67.7, 68.9, 69.1, 69.9, 72.8]]
    # print('Testing get_bridge: ', \
    #      get_bridge(bridges, 3) == expected)
