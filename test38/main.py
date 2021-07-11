# This script finds largest distance between nodes of a tree

def create_tree(alist, depthlist):
    tr = tree(alist[0])
    tr.add_depth(depthlist)
    nodes = list()
    # save the branches
    if alist[1] == None or alist[1] == []:
        nodes.append(tr)

    print("data = {}".format(alist[0]))
    for each in alist[1]:
        chld, chnodes = create_tree(each, tr.depthlist)
        tr.children.append(chld)
        nodes.extend(chnodes)

    return tr, nodes

def find_largest_distance(nodes):
    maxdist = 0
    for i in range(len(nodes)):
        print("node data = {} depthlist = {}".format(nodes[i].data, nodes[i].depthlist))
        for j in range(i, len(nodes)):
            #print("j depthlist = {}".format(nodes[j].depthlist))
            # set total distance to sum of the depth of two branches - root
            dist = len(nodes[i].depthlist) + len(nodes[j].depthlist) - 2
            # start comparing the values from the second level nodes as
            # root will always match (excluded in the dist calculation above)
            iind = len(nodes[i].depthlist) - 2
            jind = len(nodes[j].depthlist) - 2
            while iind >= 0 and jind >= 0:
                if nodes[i].depthlist[iind] == nodes[j].depthlist[jind]:
                    dist -= 2
                else:
                    break
                iind -= 1
                jind -= 1
            if dist > maxdist: maxdist = dist
    return maxdist

class tree():
    def __init__(self, data):
        # each tree node has data
        self.data = data
        # each tree node has a list of child nodes
        self.children = list()
        # store node list from this node to the root into depthlist
        self.depthlist = [data]

    def add_depth(self, list):
        # extending the depth list with the parent's depthlist
        self.depthlist.extend(list)

    def add_child(self, child):
        # append another child
        self.children.append(child)

    def add_children(self, children):
        # set the children from a list of child nodes
        self.children = children


if __name__ == '__main__':

    tlist = [1, [ [2, [[3, [[4, []]]]]], [5, [[6, []] , [7, [[8, [[9, [[10, [[11, []]] ]]]]], [12, []]]] ]], [13, []]]]
    # test tree is like this:
    #     1
    #   / | \
    # 2   5  13
    # |   | \
    # 3   6  7
    # |      |  \
    # 4      8  12
    #        |
    #        9
    #        |
    #        10
    #        |
    #        11
    tr, nodes = create_tree(tlist, [])

    print("Largest distance between nodes is {}".format(find_largest_distance(nodes)))