# This reverses a linked list partially between two values

'''
    creates a linked list from a list
    @type alist: list
    @param alist: to be converted into a linked list
'''
def create_linked_list(alist):

    head = None
    if alist == None or alist == []:
        pass
    else:
        head = node(alist[0])
        for each in alist[1:]:
            head.add_node(each)

    return head
'''
    creates a list from a linked list
    @type node: node
    @param node: head of the linked list to be converted 
'''
def create_list(node):
    alist = list()
    while node != None:
        # print("creating a list - node {}".format(node.data))
        alist.append(node.data)
        node = node.next
    return alist

'''
    reverses a linked list between two nodes in the linked list
    @type node: node
    @param node: head of the linked list
    @type a,b: int
    @param node: data of the start and stop nodes
    
'''
def reverse_list(node, a, b):
    head = node
    bnode, bnext = node.reverse(a, b, False, None)
    if node.data == a:
        head = bnode
    return head

'''
    linked list class
'''
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

        # print("node created for data={}".format(self.data))

    def add_node(self, data):
        if data == None:
            pass
        elif self.next == None:
            self.next = node(data)
        else:
            self.next.add_node(data)

    def reverse(self, a, b, rev, prev):

        bnode = bnext = None

        if self.data == b:
            if rev == True:
                # don't go deeper, just return self.next as bnext
                bnext = self.next
                # link to the preious node
                self.next = prev
                # return the self as bnode
                bnode = self

        elif self.data == a:
            if rev == True:
                bnode, bnext = self.next.reverse(a, b, rev, self)
                # continue reversing
                # point the previous node in the reversed tree
                self.next = prev
            else:
                # start reversing
                rev = True
                bnode, bnext = self.next.reverse(a, b, rev, self)
                # link to the b's next
                self.next = bnext
                # set the next to the bnode unless this is the head node
                if(prev):
                    prev.next = bnode

        elif self.next == None:
            pass
        elif rev == True:
            bnode, bnext = self.next.reverse(a, b, rev, self)
            self.next = prev
        else:
            bnode, bnext = self.next.reverse(a, b, rev, self)

        # return the node of b and next of b
        return bnode, bnext

if __name__=="__main__":

    alist = [1 ,2, 3, 4, 7, 10, 12, 15, 17, 25, 30, 35]

    ll = create_linked_list(alist)

    blist = create_list(ll)
    print("TEST#1: recreated linked list is {}".format(blist))

    head = reverse_list(ll, 4, 17)
    rlist = create_list(head)
    print("TEST#2: reversed linked list is {}".format(rlist))

    head = reverse_list(ll, 10, 35)
    rlist = create_list(head)
    print("TEST#3: reversed linked list is {}".format(rlist))

    head = reverse_list(ll, 1, 10)
    rlist = create_list(head)
    print("TEST#3: reversed linked list is {}".format(rlist))

