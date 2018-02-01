"Name: Max Tanous"
"Date: 9/21/17"
"CSCI 2320: Principles of programming languages"
"Assignment #1"
"This is a program that parses out lines of code and turns them into tokens"


import re

def main():
    
    

    #inputs the filename in and out names
    
    filename_in = input("please input the file name to read in:")
    filename_out = input("please input the file name to output to:")
    run(filename_in, filename_out)
    
def run(filename_in, filename_out):
    
    file = open(filename_out, "w")
    
    "This runs the token identifecation program"
    list_lines = open_file(filename_in)
    
    #1divides it into lines 

    for line in list_lines:
        
        split_line = split((line))
 
        for word in split_line:
            
           # runs the various checks to identify the proper tokens 
            if keyword(word):
                file.write("type" + "\t" + word + "\n")
                print ("type" + "\t" + word + "\n")
                
            elif comment(word):
                file.write("comment" + "\t" + word + "\n")
                print ("comment" + "\t" + word + "\n")
                
            elif relOp(word):
                file.write("relOp"+ "\t" + word + "\n")
                print ("relOp"+ "\t" + word + "\n") 
                
            elif eqOp(word):
                file.write("eqOp"+ "\t" + word + "\n")
                print ("eqOp"+ "\t" + word + "\n")
                
            elif multOp(word):
                file.write("multOP"+ "\t" + word + "\n")
                print ("multOP"+ "\t" + word + "\n")
                
            elif addOp(word):
                file.write("addOp"+ "\t" + word + "\n")
                print ("addOp"+ "\t" + word + "\n")
                #runs bool checks
                
            elif word == "true" or word == "false":
                file.write("boolLiteral"+ "\t" + word + "\n")
                print ("boolLiteral"+ "\t" + word + "\n")
                
            elif word == "false":
                file.write("false"+ "\t" + word + "\n")
                print ("false"+ "\t" + word + "\n")
                
            elif word == "=":
                file.write("assignOp"+ "\t" + word + "\n")
                print ("assignOp"+ "\t" + word + "\n")
                
            elif word == "while":
                file.write("while"+ "\t" + word + "\n")
                print ("while"+ "\t" + word + "\n")    
                
                #runs literal checks 
            elif word == ";":
                file.write(";"+ "\t" + word + "\n")
                print (";"+ "\t" + word + "\n")      
                
            elif word == "(":
                file.write("("+ "\t" + word + "\n")
                print ("("+ "\t" + word + "\n")
                
            elif word == ")":
                file.write(")"+ "\t" + word + "\n")
                print (")"+ "\t" + word + "\n")
                
            elif word == "=":
                file.write("="+ "\t" + word + "\n")
                print ("="+ "\t" + word + "\n") 
                
            elif word == "print":
                file.write("print"+ "\t" + word + "\n")
                print ("print"+ "\t" + word + "\n")            
                
            elif word == "main":
                file.write("main"+ "\t" + word + "\n")
                print ("main"+ "\t" + word + "\n")
                
            elif word == "{":
                file.write("{"+ "\t" + word + "\n")
                print ("{"+ "\t" + word + "\n") 
                
            elif word == "}":
                file.write("}"+ "\t" + word + "\n")
                print ("}"+ "\t" + word + "\n")
                
            elif word == "[":
                file.write("["+ "\t" + word + "\n")
                print ("["+ "\t" + word + "\n") 
                
            elif word == "]":
                file.write("]"+ "\t" + word + "\n")
                print ("]"+ "\t" + word + "\n")
                
                # checks for return statements 
            elif word == "return":
                file.write("return"+ "\t" + word + "\n")
                print ("return"+ "\t" + word + "\n")
                
            elif word == "print":
                file.write("print"+ "\t" + word + "\n")
                print ("print"+ "\t" + word + "\n") 
                
            elif ident(word):
                file.write("id" + "\t" + word + "\n")
                print ("id" + "\t" + word + "\n")                
                
            elif floatLiteral(word):
                file.write("floatLiteral" + "\t" + word + "\n")
                print ("floatLiteral" + "\t" + word + "\n")
                
            elif intLiteral(word):
                file.write("intLiteral" + "\t" + word + "\n")
                print ("intLiteral" + "\t" + word + "\n")
                
            elif charLiteral(word):
                file.write("charLiteral" + "\t" + word + "\n")
                print ("charLiteral" + "\t" + word + "\n")               
    
    
    file.close()
def open_file(filename):
    "This is a program that takes a filename as an input and reads it "
    "line by line into a list."
    open_file = open(filename)
    file = open_file.readlines()

#strips white space characters 
    for line in file:
        line = line.strip() 
    return file
  
    
    
def split(line):
    "splits line into a list of key phrases and words that can be turned to"
    "tokens"
    #lexeme splitter 
    lexemes = re.split("(//[ -~]*|==|<=|>=|-?\d*\.\d*|\W)", line)
    lexemes = [x for x in lexemes if x!= '' and x != ' ']
    return lexemes 


def keyword(word):
    "checks words for key word identification, returns true if keyword"
    if word == "bool" or word == "int" or word == "float" or word == "char":
        
        return True
    else:
        return False
        
def eqOp(word):
    "checks words for eqOp identification, returns true if equal operator"
    if word == "!=" or word == "==":
        return True
    else:
        return False  



def relOp(word):
    "checks words for relOp identification, returns true if rel operator"
    if word == "<" or  word == "<=" or  word == ">" or  word == ">=":
        return True
    else:
        return False 
    
def multOp(word):
    "checks words for MultOp identification, returns true if mult operator"
    if word == "*" or  word == "/":
        return True
    else:
        return False


def addOp(word):
    "checks words for adddOp identification, returns true if add operator"
    if word == "+" or  word == "-":
        return True
    else:
        return False

    
def floatLiteral(word):
    "checks words for float identification, returns true if float "
    
    #regex for float literal
    if re.match("\d+\.\d+", word) != None:
        return True
    else:
        return False
    
    
def intLiteral(word):
    "checks words for int identification, returns true if int "
     
     # regex for int literal
    if re.match("\d+", word) != None:
        return True
    else:
        return False

def charLiteral(word):
    "checks words for char identification, returns true if char "
    
    #matches char with regex
    if re.match("[ -~]", word) != None:
        return True
    else:
        return False
    


def ident(word):
    "checks words for ident identification, returns true if ident "


    #regex to match ident
    if re.match("[a-zA-Z]+([a-zA-Z]|\d)*", word) != None:
        return True
    else:
        return False 
    
def comment(word):
    "checks words for comment identification, returns true if comment "
   
    #looks for comment identification 
    if re.match("//([ -~]|\s)+", word) != None:
        return True
    else:
        return False 