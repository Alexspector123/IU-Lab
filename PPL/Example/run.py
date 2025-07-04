import sys, os
import subprocess
import unittest
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'D:/antlr/antlr4-4.9.2-complete.jar' # your location is going here
CPL_Dest = 'CompiledFiles'
SRC = 'Sample.g4'          #Check the file in the same directory of run.py
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')    
    print('python run.py test')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runTest():
    print('Running testcases...')
    from CompiledFiles.SampleLexer import SampleLexer

    filename ='001.txt'
    print('Running test : ' + filename)
    filepath = os.path.join(DIR, './tests', filename)      
    
    lexer = SampleLexer(FileStream(filepath)) 
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        tokens.append(token.text)
        token = lexer.nextToken()
    tokens.append('<EOF>')
    print(','.join(tokens))    
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
       
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':                    
        runTest()
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])     
    