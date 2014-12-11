from OpdsCore import OpdsProtocol
import os,sys
__author__ = 'lei'

base="c://"

class LocalOpdsProtocol(OpdsProtocol):
    """
    All Opds File System Must Realized this Class
    """

    def listBooks(self):
        """
        :return: {entiry ...}
        """
        ldir=os.listdir(base)
        for f in ldir:

            #TODO xx

        return ("No Realized")
        pass

    def dowloadBook(self):
        return ("No Realized")
        pass

    def showhtml(self):
        return ("No Realized")
        pass

