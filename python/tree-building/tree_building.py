class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def find_parent(root, p_id):
    to_visit = [root]
    while to_visit:
        node = to_visit.pop()
        if node.node_id == p_id:
            return node
        else:
            to_visit.extend(node.children)
    raise ValueError


def BuildTree(records):
    if not records:
        return None
    if not sorted([r.record_id for r in records]) == list(range(len(records))):
        raise ValueError
    records.sort(key=lambda x: (x.parent_id, x.record_id))
    root = Node(0)
    for rec in records[1:]:
        if rec.parent_id >= rec.record_id:
            raise ValueError
        node = find_parent(root, rec.parent_id)
        node.children.append(Node(rec.record_id))
    return root

