# -*- coding: utf-8 -*-
import sys
import random
from pathlib import Path

from qwordshuffle.wshuffle.wshuffle import WShuffle

sys.path.insert(0, '')

import re

from PyQt5.QtCore import (QFile, QIODevice, QTextStream)

class QWShuffle(WShuffle) :
    text_editor = None

    def __init__(self,text_edit,file_in, repeatitions=5, linesbetween=3):
        super(QWShuffle,self).__init__(file_in,repeatitions,linesbetween)
        self.text_editor = text_edit

    def cleanHtml(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def fromHtml(self):
        if not self.filename :
            return

        file = QFile(self.filename)

        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return

        text = QTextStream(file)
        text.setCodec('utf8')

        #words = self.cleanHtml(text.readAll())
        words = text.readAll()

        print('fromHtml --> ', words)

    def fromList(self,wordslst):
        self.wordslist = wordslst[:]
        self.wordslist = self.formatWords()
        self.wordslist = [s + '\n' for s in self.wordslist]
        for i in range(self.repNum):
            random.shuffle(self.wordslist)
            self.writeToFile(self.out_filename)

        out_path = Path('./' + self.out_filename)
        print('Contents saved to ', out_path.absolute())


