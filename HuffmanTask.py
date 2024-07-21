import fileinput

class Node:
    def __init__(self, probability, char, leftChild=None, rightChild=None):
        self.probability = probability
        self.char = char
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.code = ""
def CalcProbs(string):
    chars_probs = dict()
    for letter in string:
        if chars_probs.get(letter) == None:
            chars_probs[letter] = 1
        else:
            chars_probs[letter] += 1
    return chars_probs
bicodes = dict()
def setCodes(node, perantcode=""):
    mycode = perantcode + str(node.code)
    if (node.leftChild):
        setCodes(node.leftChild, mycode)
    if (node.rightChild):
        setCodes(node.rightChild, mycode)
    if (not node.leftChild and not node.rightChild):
        bicodes[node.char] = mycode
    return bicodes
def coding(string, codes):
    codeslist = []
    for letter in string:
        codeslist.append(codes[letter])
    finalcode = "".join([str(code) for code in codeslist])
    return finalcode
def StandardCommpression(string):
    char_prob = CalcProbs(string)
    letters = char_prob.keys()
    nodes = []
    for letter in letters:
        nodes.append(Node(char_prob[letter], letter))
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda major: major.probability)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        newNode = Node(left.probability + right.probability, left.char + right.char, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    codesdict = setCodes(nodes[0])
    code = coding(string, codesdict)
    return code, nodes[0]
def StandardDecommpression(binary, tree):
    root = tree
    stringlist = []
    for num in binary:
        if num == '1':
            tree = tree.rightChild
        elif num == '0':
            tree = tree.leftChild
        try:
            if tree.leftChild.char == None and tree.rightChild.char == None:
                pass
        except AttributeError:
            stringlist.append(tree.char)
            tree = root
    string = "".join([str(letter) for letter in stringlist])
    return string
string=""
for line in fileinput.input(files="test.txt"):
    string += line
print(string)
code, root = StandardCommpression(string)
print( code)
print( StandrdDecommpression(encoding, root))
