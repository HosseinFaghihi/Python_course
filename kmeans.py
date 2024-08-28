import pprint

from math import sqrt
from random import randint, choices

def extract_floats(line):
    """
    extracts floats from a line of text
    
    args:    line - a line of text
    returns: a list of floats
    """
    # Split the line into words
    words = line.split(',')
    floats = []
    for word in words:
        word = word.strip()  # Remove leading/trailing whitespace
        if word != '' and word != '?':  # Exclude empty strings and '?'
            try:
                # Try to convert the word to a float
                floats.append(float(word))
            except ValueError:
                # Ignore if the word cannot be converted to a float
                pass
    return floats

def read_float_tuples(filename):
    """
    reads a file of float tuples and returns a list of tuples
    
    args:    filename - the name of the file to read
    returns: a list of tuples
    """
    float_tuples = []
    with open(filename, 'r') as file:
        for line in file:
            # Extract floats from the line
            floats = extract_floats(line)
            # If there are at least 3 floats, create a tuple and append it to the list
            if len(floats) >= 3:
                float_tuples.append(tuple(floats[:3]))
    return float_tuples
    

points= read_float_tuples('F:\\daneshkar\\py\\points.txt')


POINT = tuple[float, float, float]

def distance(p1: POINT, p2: POINT) -> float:
    """
    calculates the distence between 2 points 
    
    args:    p1, p2 - points
    returns: distance between p1 and p2
    """
    fasele=sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
    return fasele


def k_means(points: list[POINT], centers: list[POINT]):
    """
    k-means clustering algoritm
    
    args:    points - list of points
            centers - list of centers
    returrn: list of clusters
    """
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance(point, centers[0])

        i = 1
        # for i, center in enumerate(centers):
        while i < len(centers):
            d = distance(point, centers[i])
            if d < minimum:
                index, minimum = i, d

            i += 1

        result[index]["points"].append(point)

    return result



k = int(input("K = "))
centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]
while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        x, y, z = zip(*cluster["points"])
        new_centers.append(
            (
                sum(x) / len(x),
                sum(y) / len(y),
                sum(z) / len(z),
            )
        )

    if new_centers == centers:
        break

    centers = new_centers


pprint.pprint(clusters)
