# --------------------------------------------------------------------------------
# iut info Calais : R3.02 'Développement éfficace'
# --------------------------------------------------------------------------------
# tdp1: codage/decodage Huffman
# --------------------------------------------------------------------------------
# auteur : Raphael Guarim
# date : 2022/05/28
# -------------------------------------------------------------------------------- 

# import
from __future__ import annotations
import copy
from functools import reduce

def strBin2int(str : str):
    """convertit une chaine de caractères '0'ou '1' en un entier
    
        strBin2int("10") -> 2
     """
    l : int = len(str)
    return reduce(lambda x,y: x+y[0]*2**(l-y[1]-1), [(int(j),i) for i,j in enumerate(str)],0 )
 
def int2strBin(n : int): 
    """convertit un entier en chaîne de caractères '0' ou '1' de longueur 8.

        int2strBin(2) -> '00000010'

        strBin2int(int2strBin(k)) = k 

        attention:
        int2strBin(strBin2int(s)) != s
    """
    return format(n, '08b')

def cutString(c : str, n : int):
    """coupe une chaine de caractère de longueur n*k + m  avec m<n en une liste de chaines,
       tel que longueur des k premières est égale à n et la k+1 ème est de longueur m.
    """
    res : list[str] = []
    txt = copy.deepcopy(c)
    for i in range(len(txt)//n):
        head = txt[:n] 
        txt = txt[n:]
        res.append(head)
    res.append(txt)
    return res



class Huffman:
    # class HuffmanTree
    class HuffmanTree:
        def __init__(self:Huffman.HuffmanTree,char : str | None,freq : int,left : Huffman.HuffmanTree|None=None, right : Huffman.HuffmanTree|None=None):
            """
                constructor of HuffmanTree Node

                @Args:
                    char (str) : character
                    freq (int) : frequence of character 'char'
                    left (HuffmanTree) : left child
                    right (HuffmanTree) : right child
            """
            self.char : str | None = char
            self.freq : int =freq
            self.left : Huffman.HuffmanTree|None= left
            self.right : Huffman.HuffmanTree|None= right

        def isLeaf(self : Huffman.HuffmanTree) -> bool:

            return self.left == None and self.right == None

        def strLeaf(self : Huffman.HuffmanTree, path : str|None= None):
            if path==None: path=""
            if self.isLeaf(): print(self.char,"(",self.freq,")::",path)
            else:
                if self.left: self.left.strLeaf(path+"0")
                if self.right: self.right.strLeaf(path+"1")

    @staticmethod
    def buidFreqTable(text : str):
        erreur = 0
        freqTable : list[int] = [0]*256
        for c in text: 
            freqTable[ord(c)] += 1
        return freqTable

    @staticmethod
    def insertHuffmanTreeList(tree : Huffman.HuffmanTree, list : list[Huffman.HuffmanTree]) -> list[Huffman.HuffmanTree]:
        if list == []:
            list.append(tree)
        else:
            i : int = 0
            for i,t in enumerate(list):
                if t.freq >= tree.freq: break
            list.insert(i,tree)
        return list

    @staticmethod
    def buildTreeList(freqTable : list[int]) -> list[Huffman.HuffmanTree]:
        res : list[Huffman.HuffmanTree]= []
        for i,c in enumerate(freqTable):
            if c>0: 
                node : Huffman.HuffmanTree = Huffman.HuffmanTree(chr(i),c)
                res = Huffman.insertHuffmanTreeList(node,res)
        return res

    @staticmethod
    def buildHuffmanTree(freqTable : list[int]) :

        list : list[Huffman.HuffmanTree]= Huffman.buildTreeList(freqTable)

        while len(list) != 1:
            t0 : Huffman.HuffmanTree = list[0]
            t1 : Huffman.HuffmanTree = list[1]
            list.pop(0)
            list.pop(0)
            # build new huffman tree
            nt : Huffman.HuffmanTree = Huffman.HuffmanTree(None,t0.freq+t1.freq,left=t0, right=t1)
            list = Huffman.insertHuffmanTreeList(nt,list)
        return list[0]
    
    @staticmethod
    def getCodingTable(tree : Huffman.HuffmanTree, path : str|None = None,res : dict[str,str] | None= None) -> dict[str,str]:
        if not res : res = {}
        if not path : path=""

        if tree.isLeaf():
            assert tree.char != None
            res[tree.char]=path
        else:
            if tree.left: 
                tempRes = Huffman.getCodingTable(tree.left,path+"0",res)
                for key in tempRes:
                    res[key]=tempRes[key]
            if tree.right: 
                tempRes = Huffman.getCodingTable(tree.right,path+"1",res)
                for key in tempRes:
                    res[key]=tempRes[key]
        return res
    
    @staticmethod
    def encodeHuffman(text: str) :
        freq : list[int] = Huffman.buidFreqTable(text)
        huff : Huffman.HuffmanTree = Huffman.buildHuffmanTree(freq)
        dictHuff : dict[str,str] = Huffman.getCodingTable(huff)

        coded =""
        for c in text:
            coded=coded+dictHuff[c]

        return coded,freq
    
    @staticmethod
    def encodeHuffmanByBlock(text: str, sizeBlock : int):
        # freq : list[int] = Huffman.buidFreqTable(text)
        freq : list[int] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17400,54,206,1,1,3,1,1359,93,100,9,4,1372,426,861,71,73,48,45,30,15,17,12,12,11,18,119,58,3,5,4,68,4,724,85,309,348,1398,101,82,70,714,51,4,517,281,673,512,286,129,622,754,687,599,154,11,37,29,13,3,0,3,0,0,0,7246,855,3094,3481,13980,1012,822,699,7144,517,46,5177,2816,6732,5121,2867,1292,6218,7542,6874,5988,1545,108,367,292,129,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,106,0,0,0,0,0,46,0,0,0,0,0,0,8,25,180,21,1,0,0,4,1,0,0,0,0,1,0,0,0,0,5,0,1,0,0,0,0,461,0,0,0,0,0,0,81,257,1807,213,1,0,0,43,5,0,0,0,0,10,0,0,0,0,55,0,5,0,0,0,0]
        huff : Huffman.HuffmanTree = Huffman.buildHuffmanTree(freq)
        dictHuff : dict[str,str] = Huffman.getCodingTable(huff)

        textCut : list[str] = cutString(text, sizeBlock)  # type: ignore

        blockCodes : list[str] = []
        
        for cut in textCut: 
            coded : str=""
            for c in cut:  coded=coded+dictHuff[c]
            blockCodes.append(copy.deepcopy(coded))

        return blockCodes,freq



    @staticmethod
    def decodeHuffOne(codedText :str,i :int,huff :Huffman.HuffmanTree) -> tuple[int,str | None]:
        if huff.isLeaf():
            return (i, huff.char)
        else:
            assert huff.left
            assert huff.right

            code = codedText[i]
            if code =='0':
                return Huffman.decodeHuffOne(codedText,i+1,huff.left)
            else: #code = 1
                return Huffman.decodeHuffOne(codedText,i+1,huff.right)
    
    @staticmethod
    def decodeHuff(codedText : str,huff : HuffmanTree):
        res : str  = ""
        max : int  = len(codedText)
        i : int  = 0
        while i < max:
            (i,c)= Huffman.decodeHuffOne(codedText,i,huff)
            if c != None:
                res=res+c
        return res

    @staticmethod
    def decodeHuffman(txt: str, freqs : list[int]):
        huff : Huffman.HuffmanTree = Huffman.buildHuffmanTree(freqs)
        return Huffman.decodeHuff(txt,huff)

    @staticmethod
    def bitStream2str(myTextcoded : str):

        bitStreamStr  : list[str] = cutString(myTextcoded,8) # type: ignore
        bitStreamInt : list[int]= list(map(strBin2int, bitStreamStr)) # type: ignore
        codedText : str = "".join(list(map(chr,bitStreamInt)))

        return codedText, len(myTextcoded)

    @staticmethod
    def str2bitStream(txt : str, length: int):
        bitStream : str = "".join(map(int2strBin,[ord(c) for c  in txt])) # type: ignore
        # last char can be false
        head : str = bitStream[:-8]
        tail : str =bitStream[-8:]
        
        # compare with original 
        nbBit : int = len(bitStream) - length
        if nbBit != 0 :
            # remove '0' at the beginning
            bitStream = head+tail[nbBit:]

        return bitStream
# --------------------------------------------------------------------------------
# main : some  tests
# --------------------------------------------------------------------------------
if __name__ == '__main__':
    
    myText= "Souvent, pour s'amuser, les hommes d'équipage Prennent des albatros, vastes oiseaux des mers, Qui suivent, indolents compagnons de voyage, Le navire glissant sur les gouffres amers. \
À peine les ont-ils déposés sur les planches, Que ces rois de l'azur, maladroits et honteux, Laissent piteusement leurs grandes ailes blanches \
Comme des avirons traîner à côté d'eux. Ce voyageur ailé, comme il est gauche et veule ! Lui, naguère si beau, qu'il est comique et laid ! L'un \
agace son bec avec un brûle-gueule, L'autre mime, en boitant, l'infirme qui volait ! \
Le Poëte est semblable au prince des nuées Qui hante la tempête et se rit de l'archer , Exilé sur le sol au milieu des huées, \
Ses ailes de géant l'empêchent de marcher."

    print(">> test Huffman: text to be encoded")
    print(">> ----------------------------------------")
    print(myText)
    print(">> ----------------------------------------")

    # encoding en convert to txt
    bitStream,freqTable  = Huffman.encodeHuffman(myText)
    myTextcoded, length = Huffman.bitStream2str(bitStream)


    print(">> encoded text according Huffman")
    print("----------------------------------------")
    print(f'{myTextcoded}')
    print("----------------------------------------")

    # decoding
    newBitStream = Huffman.str2bitStream(myTextcoded, length) 
    decoded = Huffman.decodeHuffman(newBitStream, freqTable)

    print(">> decoded text")
    print(">> ----------------------------------------")
    print(decoded)
    print(">> ----------------------------------------")
    print(f'>> compression ratio: {round(100*len(myTextcoded)/len(myText))} %')


