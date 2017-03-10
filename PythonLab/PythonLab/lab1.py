import argparse
import re

class Graph:
    def __init__(self):
        self.vertices = set()

    def add(self, id):
        setContainsValue = False
        

class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = set()
    
    # Checks through the set of adjacent vertices to see if we already have an edge from this vertex to 
    # it, if we do we just increment it's weight, if not make a new one
    def addEdge(self, vertex):
        setContainsValue = False
        for edge in self.edges:
            if vertex.id == edge.vertex.id:
                setContainsValue = True
                edge.weight += 1

        if not setContainsValue:
            edge = Edge(vertex)
            self.edges.add(edge)

class Edge:
    def __init__(self, vertex):
        self.vertex = vertex
        self.weight = 0

        

# Replace the string value of the following variable with your names.
ME = 'Sean White';
COLLABORATORS = ['nobody']

def process_file(infile):
    titles = set()

    # Loop through each line of the file
    for line in infile:
        # I removed the print function to make my output easier to debug, I ended up doing more than was required 
        # for the regex as there was still a few weird things in my output that needed to be cleaned up without it
        line = re.sub( r'.*>|[.|?|&|;|!|_|/|0-9|#]|\(.*|\[.*|".*|:.*|feat.*|featuring.*| - .*|{.*', '', line )
        line = re.sub( r'-|  ', ' ', line )
        
        # added each line to the titles set in lowercase without the trailing whitespace
        titles.add( line.lower().rstrip() )

    # loop over the cleaned titles and compute the bigram counts
    # I ended up using a custom built directional graph to track the occurence of words, it seemed easiest to build the extra
    # credit assignment that way since we can hold the value as the weight of the edge between them and simply follow the
    # heaviest path n jumps to get the generated song title, plus bfs makes it relatively quick to search.
    wordGraph = Graph()
    for title in titles:
        words = title.split()
        for word in words:
            print(word)


    # using bigram_count, find most common word following 'word'
    # Her name is wordGraph now
    def most_common_word(word):
        return random.choice(choices)

    # return most common word
    return most_common_word


# DON'T WORRY ABOUT CODE BELOW HERE, IT JUST MAKES YOUR LIVE EASIER
# I ended up having to worry, more details below
def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    return parser.parse_args().file_name


def main():
    print ('CSCI 305 Lab 1 submitted by {}'.format(ME))
    print ('  with help from %s\n\n' % ', '.join(COLLABORATORS))
    file_name = get_file_name()
    #Had to add the encoding, was getting errors reading the file in Python3 without it
    with open(file_name, 'r', encoding='utf8') as infile:
        process_file(infile)


if __name__ == '__main__':
    main()