from json import dumps


class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def pathfind(self, dict_, target, path=()):
        for k, v in dict_.items():
            path = path + (k,)
            if k == target:
                return path
            elif v:
                for subdict in v:
                    subpath = self.pathfind(subdict, target, path)
                    if subpath:
                        return subpath
        return None

    def pathTo(self, from_node, to_node):
        dict_ = self.__dict__()
        p_from = self.pathfind(dict_, from_node)
        p_to = self.pathfind(dict_, to_node)
        if not (p_from and p_to):
            raise ValueError(f'node {from_node if p_to else to_node} does not exist')
        while p_from and p_to and p_from[0] == p_to[0]:
            cn = p_from[0]
            p_from = p_from[1:]
            p_to = p_to[1:]
        return list(tuple(reversed(p_from)) + (cn,) + p_to)

    def subdict(self, node):
        dict_ = self.__dict__()
        path = list(self.pathfind(dict_, node))
        subdict = dict_[path.pop(0)]
        while path:
            nc = path.pop(0)
            for child in subdict:
                if nc in child.keys():
                    subdict = child[nc]
                    continue
        return {node: subdict}

    def dictFromPov(self, from_node):
        dict_ = self.__dict__()
        path = self.pathfind(dict_, from_node)
        if path:
            path = list(path)
        else:
            raise ValueError(f'node {from_node} does not exist')
        inv_pairs = list(zip(path, path[1:]))
        acc_dict = []
        while inv_pairs:
            nb, nt = inv_pairs.pop(0)
            nbc = self.subdict(nb)[nb]
            nbc = [ch for ch in nbc if nt not in ch.keys()]
            nbc.extend(acc_dict)
            acc_dict = [{nb: nbc}]
        acc_sibs = self.subdict(from_node)[from_node]
        return {from_node: acc_dict + acc_sibs}

    def dictToTree(self, dict_):
        k, v = list(dict_.items())[0]
        return Tree(k, [self.dictToTree(ch) for ch in v])

    def fromPov(self, from_node):
        return self.dictToTree(self.dictFromPov(from_node))