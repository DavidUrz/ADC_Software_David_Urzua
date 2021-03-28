# David Urzua A00354893
import argparse

parser = argparse.ArgumentParser(description="Name of file to analyse")
parser.add_argument("FileName", type=str,
                    help="File name, must be .txt in same forlder")
args = parser.parse_args()


def readFile(fileName):
    wordFreq = {}
    sorted_wordFreq = {}
    with open(fileName) as filetxt:
        for line in filetxt:
            for word in line.split():
                if word.isalpha():
                    count = wordFreq.get(word, 0)
                    wordFreq[word] = count + 1
    sorted_keys = sorted(wordFreq, key=wordFreq.get, reverse=True)  # sorted_keys is a list
    for w in sorted_keys:
        sorted_wordFreq[w] = wordFreq[w]
    return sorted_wordFreq


sorted_Dict = readFile(args.FileName)
word = (input("Type the word you want to find\n"))
print("The word: '{}' appeard {} times".format(word, sorted_Dict.get(word, 0)))
