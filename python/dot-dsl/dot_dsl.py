NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


def validate_graph_data(data):
    if not type(data) == list or min(map(len, data)) < 3:
        raise TypeError
    for k, *d in data:
        dtypes = list(map(type, d))
        if k not in (ATTR, NODE, EDGE):
            raise ValueError
        elif k == ATTR and not dtypes == [str, str]:
            raise ValueError
        elif k == NODE and not (dtypes == [str, dict] or
                              dtypes == [str, set]):
            raise ValueError
        elif k == EDGE and not dtypes == [str, str, dict]:
            raise ValueError


class Graph(object):
    def __init__(self, data=[]):
        self.attrs = {}
        self.nodes = []
        self.edges = []
        if data:
            validate_graph_data(data)
            self.assign(data)

    def assign(self, data):
        for k, *d in data:
            if k == ATTR:
                self.attrs[d[0]] = d[1]
            elif k == NODE:
                self.nodes.append(Node(*d))
            elif k == EDGE:
                self.edges.append(Edge(*d))
