from math import sqrt
from random import randint
import pprint

class KMeansClustering:
    def __init__(self, points):
        self.points = points

    def distance(self, p1, p2):
        """
        calculates the distance between two points
        args:    p1, p2 - points
        returns: distance between p1 and p2
        """
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

    def k_means(self, centers):
        """
        k-means clustering algorithm
        args:    centers - list of center points
        returns: list of clusters
        """
        result = [
            {
                "center": center,
                "points": [],
            }
            for center in centers
        ]
        for point in self.points:
            index, minimum = 0, self.distance(point, centers[0])

            i = 1
            while i < len(centers):
                d = self.distance(point, centers[i])
                if d < minimum:
                    index, minimum = i, d

                i += 1

            result[index]["points"].append(point)

        return result

if __name__ == "__main__":
    def extract_floats(line):
        """
        extracts floats from a line of text
        args:    line - a line of text
        returns: a list of floats
        """
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

    points = read_float_tuples('F:\\daneshkar\\py\\points.txt')

    k = int(input("K = "))
    centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(k)]

    kmeans = KMeansClustering(points)
    while True:
        clusters = kmeans.k_means(centers)
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
