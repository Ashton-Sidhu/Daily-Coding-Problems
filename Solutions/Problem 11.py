#QUESTION
#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

#Solution
#Use a trie to preprocess words and then return all words, defined by isWord
#of the trie starting at the node with the given prefix.

#Time Complexity: O(N) - only going through the trie once.

class _Node:
        
    #Does this node represent the last character in a word?
    isWord = False
        
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.children = {}

_trie = _Node()

def Autocomplete(li):
    '''
    Take a list of words and compose a trie.
    '''
    _trie = _Node("")
    for item in li:
        _InsertWord(item)

def _InsertWord(s):
    '''
    Private function that turns a word into a sub tree of a trie.
    '''
    curr = _trie

    for i,char in enumerate(s):
        if char not in curr.children.keys():
            curr.children[char] = _Node(s[0:i+1])
        curr = curr.children[char]
        if i == len(s) - 1: curr.isWord = True

def GetWords(prefix):
    '''
    Function that finds all words for a given prefix.
    '''
    words = []

    if prefix is "": return words

    curr = _trie

    for char in prefix:
        if char in curr.children.keys():
            curr = curr.children[char]
        else:
            return words

    _GetWords(curr, words)
    return words
    
def _GetWords(n, words):
    '''
    Private helper function that recursively goes through the trie
    and finds words given the prefix.
    '''
    if n.isWord: words.append(n.prefix)
    for char in n.children.keys():
        _GetWords(n.children[char], words)

def main():
    Autocomplete(['dog', 'deer', 'deal'])
    
    assert(GetWords("de") == ['deer', 'deal'])
    assert(GetWords("") == [])

if __name__ == '__main__':
    main()