""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
items = {}
def checkBST(node, minV=0, maxV=0):
    global items
    if     (node==None or node.data in items.keys()) \
        or (node.left!=None and (node.data<=node.left.data or (minV!=0 and node.left.data<minV))) or (node.right!=None and (node.data>=node.right.data or (maxV!=0 and node.right.data>maxV))):
        return False
    items[node.data] = False
    
    if      (node.left==None or (node.left!=None and checkBST(node.left, minV, node.data))) \
        and (node.right==None or (node.right!=None and checkBST(node.right, node.data, maxV))):
        return True
    return False

'''

def checkBST(node):
    print("pNode:%s, lNode:%s, rNode:%s" % (node.data, node.left.data if node.left!=None else "None", node.right.data if node.right!=None else "None"))
    if node.left!=None:
        checkBST(node.left)
    if node.right!=None:
        checkBST(node.right)


      3
   2     6
 1   4 5   7

pNode=3 lNode:2 rNode:6
pNode=6 lNode:5 rNode:7
pNode=7 lNode:None rNode:None
done pNode:7
pNode=5 lNode:None rNode:None
done pNode:5
done pNode:6
pNode=2 lNode:1 rNode:4
pNode=4 lNode:None rNode:None
done pNode:4
pNode=1 lNode:None rNode:None
done pNode:1
done pNode:2
done pNode:3
No



      4
   2     6
 1   3 5   7

pNode=4 lNode:2 rNode:6
pNode=6 lNode:5 rNode:7
pNode=7 lNode:None rNode:None
done pNode:7
pNode=5 lNode:None rNode:None
done pNode:5
done pNode:6
pNode=2 lNode:1 rNode:3
pNode=3 lNode:None rNode:None
done pNode:3
pNode=1 lNode:None rNode:None
done pNode:1
done pNode:2
done pNode:4
No

4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31

                                                                          17
                                           8                                                          24
                         4                                12                             20                           28
                   2           6                   10             14             18             22            26               30
               1       3   5      7            9      11     13        15    16       19   21        23  25        27     29         31
pNode:17, lNode:8, rNode:24
pNode:8, lNode:4, rNode:12
pNode:4, lNode:2, rNode:6
pNode:2, lNode:1, rNode:3
pNode:1, lNode:None, rNode:None
pNode:3, lNode:None, rNode:None
pNode:6, lNode:5, rNode:7
pNode:5, lNode:None, rNode:None
pNode:7, lNode:None, rNode:None
pNode:12, lNode:10, rNode:14
pNode:10, lNode:9, rNode:11
pNode:9, lNode:None, rNode:None
pNode:11, lNode:None, rNode:None
pNode:14, lNode:13, rNode:15
pNode:13, lNode:None, rNode:None
pNode:15, lNode:None, rNode:None
pNode:24, lNode:20, rNode:28
pNode:20, lNode:18, rNode:22
pNode:18, lNode:16, rNode:19
pNode:16, lNode:None, rNode:None
pNode:19, lNode:None, rNode:None
pNode:22, lNode:21, rNode:23
pNode:21, lNode:None, rNode:None
pNode:23, lNode:None, rNode:None
pNode:28, lNode:26, rNode:30
pNode:26, lNode:25, rNode:27
pNode:25, lNode:None, rNode:None
pNode:27, lNode:None, rNode:None
pNode:30, lNode:29, rNode:31
pNode:29, lNode:None, rNode:None
pNode:31, lNode:None, rNode:None
No
'''