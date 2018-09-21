# -*- coding: utf-8 -*-

#!/usr/bin/python3

import sys
import io
import random
from pathlib import Path  # for is_file function
from subprocess import check_call

# from PyQt5.QtPrintSupport import QPrintDialog, QPageSetupDialog, QPrintPreviewDialog, QPrinter,QPrintPreviewWidget
# from PyQt5.QtWidgets import QApplication

class WShuffle :
    lines = 3
    filename = ''
    out_filename = ''
    wordslist = []
    repNum = 3
    def __init__(self, file_in, repeatitions=5, linesbetween=3):
        self.lines = linesbetween;
        self.repNum = repeatitions
        self.filename = file_in
        self.out_filename = file_in[:-4] + '_out.txt'


    def write(self):
        self.writeToFile(self.filename)

    def writeToFile(self,filename):
        try :
            with io.open(filename, 'a', encoding='utf8') as f :
                count = 1
                for s in self.wordslist :
                    word = '{:4d}'.format(count) + '. ' + s + '\n'
                    # print(word)
                    f.write(word)
                    count += 1

                for i in range(self.lines):
                    f.write('\n')
        except FileNotFoundError as fnf :
            print('Σφάλμα τύπου ', fnf,'Δεν υπάρχει τέτοιο αρχείο.')
        except :
            print('Γενικό σφάλμα:  Σφάλμα στη διαχείρηση αρχειου')


    def readFirstNLines(self,filename, N=None):
        contents = []
        try :
            print('Reading {}'.format(filename))
            with open(filename, encoding='utf8') as myfile:
                contents = myfile.read().splitlines()

            if N :
                if len(contents) >= N :
                    self.wordslist = contents[:N]
                    return self.wordslist
                else:
                    print('Index out of bounds!')
                    return []
            else:
                self.wordslist = contents[:]
                return  self.wordslist

                #head = [next(myfile) for x in range(N)]
        except FileNotFoundError as fnf :
            print('Σφάλμα τύπου ', fnf, 'Δεν υπάρχει τέτοιο αρχείο.')
        except :
            print('Γενικό σφάλμα:  Σφάλμα στη διαχείρηση αρχειου')

    def read(self, lines=None):
        return self.readFirstNLines(self.filename, lines)

    def formatWords(self):
        equalto = '->_______________________'
        sz = [len(w) for w in self.wordslist]
        max_len = max(sz)
        self.wordslist = [w + (max_len - len(w) + 2) * '.' + equalto for w in self.wordslist]
        return self.wordslist

    def shuffle_from_file(self, filename, lines=None):
        self.wordslist = self.readFirstNLines(self.filename,lines)
        self.wordslist = self.formatWords()
        self.wordslist = [s + '\n' for s in self.wordslist]
        for i in range(self.repNum) :
            random.shuffle(self.wordslist)
            self.writeToFile(self.out_filename)

        out_path = Path('./' + self.out_filename)
        print('Contents saved to ', out_path.absolute())

    def shuffle(self, lines=None):
        self.shuffle_from_file(self.filename,lines)
