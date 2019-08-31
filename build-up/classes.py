eID = 0

class MathSum(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.pairChar = ""
        self.children = []
        self.power = None
        self.result = 0
        self.origin = None
        self.dividing = False

class MathProduct(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.modifier = 1
        self.children = []
        self.origin = None
        self.power = None


class MathElement(object):
    def __init__(self):
        global eID
        self.id = eID
        eID += 1
        self.contentString = ""
        self.contentNumber = 0
        self.origin = None
        self.power = None
        self.children = []
        self.dividing = False

def expandExp(root, indent):
    itemOriginID = -1
    if root.origin != None:
        itemOriginID = root.origin.id
    if type(root) == MathSum:
        print(' '*indent + "Sum (id: " + str(root.id) + "), isDividing =", root.dividing, ", type: " + root.pairChar + " origin: " + str(itemOriginID))
    elif type(root) == MathProduct:
        print(' '*indent + "Product (id: " + str(root.id) + "), modifier: " + str(root.modifier) + " origin: " + str(itemOriginID))
    elif type(root) == MathElement:
        print(' '*indent + "Element (id: " + str(root.id) + "): [ " + root.contentString + " ], isDividing =", root.dividing, " origin: " + str(itemOriginID))
    if root.power != None:
        print(' '*indent + ", with Power {")
        expandExp(root.power, indent + 3)
        print(' '*indent + "}")
    for child in root.children:
        expandExp(child, indent + 3)


ansStr = ""


def printExp(root):
    global ansStr
    ansStr = ""
    _printExp(root)
    print(ansStr)


def _printExp(root):
    global ansStr
    if type(root) == MathSum:
        if root.pairChar == "(":
            ansStr += "("
        isFirstItem = True
        for child in root.children:
            if isFirstItem:
                if child.modifier == -1:
                    ansStr += "-"
            else:
                ansStr += "+" if child.modifier == 1 else "-"
            isFirstItem = False
            _printExp(child)
        if root.pairChar == "(":
            ansStr += ")"
        if root.power != None:
            ansStr += "^"
            _printExp(root.power)
    elif type(root) == MathProduct:
        isFirstItem = True
        for child in root.children:
            if isFirstItem == False:
                ansStr += "/" if child.dividing == 1 else "*"
            isFirstItem = False
            _printExp(child)
    else:
        ansStr += root.contentString
        if root.power != None:
            ansStr += "^"
            _printExp(root.power)

