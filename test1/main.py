# This script clones an undirected graph represented with a label and list of neighboring nodes
#
# This script is a part of the Easy Python project which creates a number
# sample python scripts to answer simple programming questions. The
# entire project is accessible at https://github.com/okany/easypython.
# Copyright (c) 2021 Okan Yilmaz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
class gnode_list():
    def __init__(self, nlist, llist):
        self.nlist = nlist
        self.llist = llist
        self.nodes = dict()
        self.links = []
        self.create_nodes()
        self.create_links()

    def create_nodes(self):
        for each in self.nlist:
            if each not in self.nodes:
                ug = gnode(each)
                self.nodes[each] = ug

    def create_links(self):
        for each in self.llist:
            if(each[0] and each[1] and each[0] in self.nodes and each[1] in self.nodes):
                # print("creating a link between {} and {}".format(each[0], each[1]))
                e0 = self.nodes[each[0]]
                e1 = self.nodes[each[1]]
                self.link_ugraphs(e0, e1)
                self.links.append([e0, e1])

    def print_nodes(self):
        print("PRINTING NODES")
        for each in self.nodes.values():
            each.print_node()

        print("PRINTING LINKS")
        for each in self.links:
            print("nodeA = {} nodeA.label = {}, nodeB = {} nodeB.label = {}".
                  format(each[0], each[0].label, each[1], each[1].label))

    def link_ugraphs (self, ga, gb):
        ga.add_neigh(gb)
        gb.add_neigh(ga)

    def unlink_ugraphs (self, ga, gb):
        ga.delete_neigh(gb)
        gb.delete_neigh(ga)

    def get_node(self, label):
        node = None
        if label in self.nodes:
            node = self.nodes[label]
        return node
#
# this class is used to clone an undirected graph from a node in the graph
# note that this function does not utilize gnode_list graph on purpose
#
class clone_ugraph():
    def __init__(self, anode):
        self.nodes = dict()
        self.cnode = self.clone_ugraph(anode)
        self.pnodes = dict() # used during printing the nodes

    def clone_ugraph(self, anode):
        bnode = None
        if(anode.label not in self.nodes):
            bnode = gnode(anode.label)
            # save the orig node and clone in the nodes dict
            self.nodes[anode.label] = [anode, bnode]
            for each in anode.neigh:
                bneigh = self.clone_ugraph(each)
                bnode.add_neigh(bneigh)
        else:
            # retrieve the bnode saved in the nodes dict
            bnode = self.nodes[anode.label][1]
        return bnode

    def print_cnode(self, cnode):

        if cnode.label not in self.pnodes:
            self.pnodes[cnode.label] = cnode
            cnode.print_node()
            for each in cnode.neigh:
                self.print_cnode(each)

    def print_clone(self):
        print("PRINTING CLONED NODES")
        self.pnodes = dict()
        self.print_cnode(self.cnode)

    def get_clone(self):
        return self.cnode

class gnode():
    def __init__(self, label):
        self.label = label
        self.neigh = []

    def add_neigh(self, neigh):
        if type(neigh) == gnode and neigh not in self.neigh:
            self.neigh.append(neigh)
        else:
            print("add_neigh: incorrect type")

    def delete_neigh(self, neigh):
        if type(neigh) == gnode and neigh in self.neigh:
            self.neigh.remove(neigh)
        else:
            print("delete_neigh: incorrect type")

    def print_node(self):
        neighs = ""
        for each in self.neigh:
            neighs += each.label + ","
        if(len(neighs)):
            neighs = neighs[:-1]
        print("node: {}, label: {}, neighs: {}".format(self, self.label, neighs))

if __name__ == "__main__":

    nlist = ["a", "b", "c", "d", "e", "f"]
    llist = [["a", "b"], ["a", "c"], ["c", "d"], ["c", "f"], ["d", "f"]]

    gnl = gnode_list(nlist, llist)
    gnl.print_nodes()

    anode = gnl.get_node("a")
    cug = clone_ugraph(anode)
    # note that "e" is not printed since it is not connected to the cluster which was cloned
    cug.print_clone()

    nlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    llist = [["a", "b"], ["a", "c"], ["c", "d"], ["c", "f"], ["d", "f"], ["e", "g"], ["h", "i"], ["g", "h"]]

    gnl = gnode_list(nlist, llist)
    gnl.print_nodes()

    anode = gnl.get_node("a")
    cug = clone_ugraph(anode)
    # note that "e", "g", "h", "i" are not printed since it is not connected to the cluster which was cloned
    cug.print_clone()

    anode = gnl.get_node("g")
    cug = clone_ugraph(anode)
    # note that "a", "b", "c", "d", "f" are not printed since it is not connected to the cluster which was cloned
    cug.print_clone()


