from fiona import collection


def read_txt(filename):
    """Read a text file and return a lit of rows

    Args:
        filename (str): path to file to open
    Returns:
        list of lines from text file
    """
    with open(filename, 'r') as lines:
        return lines.readlines()

def write_shape(filename, schema, data):
    """Write to filename based on schema as ESRI shapefile format.

    Args:
        filename (str): path to output file
        schema (dict): data scheme
        data (list): list of dicts with data
    """
    with collection(filename, "w", "ESRI Shapefile", schema) as output:
        for row in data:
            print row
            output.write(row)
    
