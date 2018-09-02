class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.name = False
        self.children = [None for i in range(26)]


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        """
        Inserts a name into the trie.
        :type name: str
        :rtype: void
        """
        trav = self.root
        for c in name:
            index = ord(c) - ord('a')
            if trav.children[index] == None:
                trav.children[index] = TrieNode()
                trav = trav.children[index]
            else:
                trav = trav.children[index]
        trav.name = True

    def search(self, name):
        """
        Returns if the name is in the trie.
        :type name: str
        :rtype: bool
        """
        trav = self.root
        for c in name:
            index = ord(c) - ord('a')
            if trav.children[index] != None:
                trav = trav.children[index]
            else:
                return False
        if trav.name:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any name in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trav = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if trav.children[index] != None:
                trav = trav.children[index]
            else:
                return False
        return True

    def suggest(self, prefix):
        """
        Prints all names possible given a prefix
        """
        trav = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if trav.children[index] != None:
                trav = trav.children[index]
            else:
                print "prefix not found"
        return self.traverse(trav, prefix)
    def traverse(self,trav, prefix):
        if trav.name:
            print prefix
        for i , node in enumerate(trav.children):
            if node != None:
                self.traverse(node, prefix+chr(i+ord('a')))
        return
trie = Trie()
trie.insert("ab")
trie.insert("ac")
trie.insert("ca")
trie.insert("abacus")
trie.insert("ad")
trie.insert("azhar")
trie.insert("aksar")
trie.insert("jacob")
trie.insert("jake")
trie.insert("judy")
trie.insert("jennifer")
print "a found" , trie.search("a")
print "startsWith" , trie.startsWith("a")
print "----"
print "stuff starting with ab"
trie.suggest("ab")
print "----"
print "friends with J"
trie.suggest("j")
print "----"
print "friends starting with jen"
trie.suggest("jen")
