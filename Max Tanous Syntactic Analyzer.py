"This program is a syntactic analyzer that takes in a string of lexemes." 
"and analyzes in it a recursive decent parsing fashion."
" Full submission For Principles of Prgramming Languages"
"Name: Max Tanous"
"Date: 10/18/17"



def main():
    
    
    file_Name = input("Please enter the file name: ")
    #global variables 
    global consumedLexemes, consumedTokens, indexToken
    consumedTokens =[]
    consumedLexemes = []

    
    #Process the input file and build lists of tokens and lexemes
    file = open(file_Name, "r")
    read_file = file.read()
    List = read_file.split() #bigList is a list of tokens and lexemes (alternating)
    consumedTokens = List[0::2] #List of tokens sliced from bigList (even elements)
    lexemes = List[1::2] #List of lexemes
    
    #runs the program
    indexToken = program()
    
    
    #condition for valid grammar 
    if indexToken == len(consumedTokens) - 1:
        print("Syntactically Correct")
       
    else:
        error(indexToken) # failed grammar
    
def program():
    
    #initializes index token
    indexToken = 0
    if consumedTokens[indexToken] == "type":  # checks essential key words
        indexToken += 1
        if consumedTokens[indexToken] == "main":
            indexToken += 1
            if consumedTokens[indexToken] == "(":
                indexToken += 1
                if consumedTokens[indexToken] == ")":  
                    indexToken += 1
                    if consumedTokens[indexToken] == "{":
                        indexToken += 1
                        if declerations(indexToken) != indexToken: # runs checks for Declerations
                            indexToken = declerations(indexToken)
                            if statements(indexToken) != indexToken: # runs checks fpr Statments
                                indexToken = statements(indexToken)
                                if consumedTokens[indexToken] == "{": # checks last nessecary element 
                                    indexToken += 1
                                    return indexToken
   
   
   
   
   
    
    return indexToken

   
   
  
    

     
def declerations(token):
    "checks for declration"
     
     # while loop to ocmplete decleration checks 
    while token < len(consumedTokens) and decleration(token) != token:
        #updates token
        token = decleration(token)
    return token
          
def decleration(token):
    
    
    holder = token # holder variable in case of failure
    
    if token < len(consumedTokens) and consumedTokens[token] == "type":
        
        token += 1
        if token < len(consumedTokens) and consumedTokens[token] == "id": # checking nessecary tokens and consuming them
            
            token += 1
            while token < len(consumedTokens) and consumedTokens[token] == "id":
                    # updating the consumed tokens 
                    token += 1
                   
            
            if token < len(consumedTokens) and consumedTokens[token] == ";":
                token += 1
              # valid decleration grammar 
                return token 
    
    else:
        #failed grammar 
        return holder

def statements(token):
    "checks the Statments grammar by callign statment" 
    
    # statements check
    while token < len(consumedTokens) and statement(token) != token:
        #updates token based on statements 
        token = statement(token)
    return token    
     
def statement(token):
    "Statment Grmamar checks" 
    
    if token < len(consumedTokens) and assignment(token) != token: # assignment check
        token = assignment(token)
        return token
    if token < len(consumedTokens) and ifStatement(token) != token: # if statement check
        token = ifStatement(token)
        return token
    if token < len(consumedTokens) and printStmnt(token) != token: # print statement check
        token = printStmnt(token)
        return token
    if token < len(consumedTokens) and whileStmnt(token) != token: # while statement check
        token = whileStmnt(token)
        return token
    if token < len(consumedTokens) and returnStmnt(token) != token: # return Statement check
        token = returnStmnt(token)
        return token    
    
    # no grammar found
    return token    

def printStmnt(token):
    " Checks print Statement Grammar " 
    # case of failed grammar checks 
    holder = token
    if token < len(consumedTokens) and consumedTokens[token] == "print":
        #consumes tokens 
        token += 1
        if token < len(consumedTokens) and expression(token) != token:
            #Updates from expression grammar check 
            token = expression(token)
            if token < len(consumedTokens) and consumedTokens[token] == ";":
                token += 1 # consumes token
                
                
                return token
        
   
   
   
    return holder #failed grammar check for print Statment 
        
     
def ifStatement(token):
    " If statment check"
    
    check = False # nessecary because of the possible optional option
    holder = token
    if token < len(consumedTokens) and consumedTokens[token] == "if":
        token += 1 # consuming tokens 
        if token < len(consumedTokens) and consumedTokens[token] == "(":
            token += 1 # consuming tokens    
            if token < len(consumedTokens) and expression(token) != token:
                token = expression(token) # expression grammar check update 
                
                
                if token < len(consumedTokens) and consumedTokens[token] == ")":
                    token += 1 #consumes token
                
                    if token < len(consumedTokens) and statement(token) != token:
                      
                        token = statement(token) # updates tokens
                        
                        check = True
                        if token < len(consumedTokens) and consumedTokens[token] == "else" and statements(token + 1) != token:
                            
                            token += 1
                            token = statements(token) # updating token statement 
                            return token
                            
    
    if check: # optional condition not met but other grammar met 
      
        return token
   
   
  
    return holder # grammar failed 
        
    

def whileStmnt(token):
    "While Statement Grammar Check"
    
    
    
    holder = token # case of failed grammar 
    if token < len(consumedTokens) and consumedTokens[token] == "while":
        token += 1 # consume token 
        if token < len(consumedTokens) and consumedTokens[token] == "(":
            token += 1   
            if token < len(consumedTokens) and expression(token) != token:
                token = expression(token) #expression grammar check 
                if token < len(consumedTokens) and consumedTokens[token] == ")":
                    token += 1 # consume token
                    if token < len(consumedTokens) and statement(token) != token:
                        token = statement(token) # statement grammar check
                        return token

    
    
    return holder

def returnStmnt(token):
    "return Statment check" 
    
    
    holder = token # case of holder 
    
    if token < len(consumedTokens) and consumedTokens[token] == "return":
        token += 1    # consume token 
        if token < len(consumedTokens) and expression(token) != token:
            token = expression(token) #expression gramamr check 
            if token < len(consumedTokens) and consumedTokens[token] == ";":
                token += 1 # consume token
                return token
            
     
     
    return holder   # failed grammar check

def assignment(token):
    
    holder = token # case of failed grammar 
    
    if token < len(consumedTokens) and consumedTokens[token] == "id":
        
        token += 1 # consumign tokens
        if token < len(consumedTokens) and consumedTokens[token] == "assignOp":
            
            token += 1 # consuming token
            if token < len(consumedTokens) and expression(token) != token:
                
                token = expression(token) #expression grammar check 
                if token < len(consumedTokens) and consumedTokens[token] == ";":
                    token += 1
                    return token #valid grammar!
                  
                  
    return holder # failed Grammar 



     
    
def expression(token):
    "Expression grammar Check"
    holder = token # in case of failed grammar 
    
    if token < len(consumedTokens) and conjunction(token) != token:
        token = conjunction(token) #update token consumption
        while token < len(consumedTokens) and consumedTokens[token] == "||" and\
        conjunction(token+1) != token + 1:
            token += 1
            token = conjunction(token) # optional while loop
        return token

    
    
    return holder #failed gramamr 
    
def conjunction(token):
    "conjuction grammar check" 
    
    holder = token # case of failed grammar 
    if token < len(consumedTokens) and equality(token) != token:
        token = equality(token) # equality update. 
        while token < len(consumedTokens) and consumedTokens[token] == "&&" and\
        conjunction(token+1) != token + 1:
            token += 1
            token = conjunction(token)
        return token # conjuction succcess grammar 
   
     
     
    return holder    # grammar failed
    

def equality(token):
    "equality grammar checks "
    
    check = False # check for optional grammar 
    holder = token
    if token < len(consumedTokens) and relation(token) != token:
        token = relation(token)
        check = True # nessecary grammar met 
        if token < len(consumedTokens) and consumedTokens[token] == "equOp" and relation(token + 1) != token + 1:
            
            token += 1
            token = relation(token) # token updated
            return token
    if check:
        return token # nessecary grammar but not optional
    
    
    return holder # failed grammar 



def relation(token):
    "Relation grammar"
    
    check = False # optional grammar conditional
    holder = token
    if token < len(consumedTokens) and addition(token) != token: 
        token = addition(token) #updates token
        check = True # nessecary grammar met
        if token < len(consumedTokens) and consumedTokens[token] == "relOp"\
           and token + 1 < len(consumedTokens) and addition(token + 1) != token + 1\
           :
            token += 1
            token = addition(token) # consuming tokens 
            return token
    
    if check:
        return token # optional grammar met 
     
    return holder #failed grammar 
        


def addition(token):
    "check for addition grammar"
    
    holder = token
    if token < len(consumedTokens) and term(token) != token:
        token = term(token) # consuming tokens from term gramamr 
        while token < len(consumedTokens) and consumedTokens[token] == "addOp"\
              and token + 1 < len(consumedTokens) and term(token + 1) != token + 1:
            token += 1
            token = term(token)
            
        
        return token # grammar met 
    
    return holder # gramamr failed 



def term(token):
    "term grammar checks "
    
    holder = token # case of invalid grammar 
    if token < len(consumedTokens) and factor(token) != token:
        token = factor(token)
        while token < len(consumedTokens) and consumedTokens[token] == "multOp"\
              and token + 1 < len(consumedTokens) and factor(token + 1) != token + 1:
            
            token += 1  # consume token
            
            token = factor(token) # consume tokens from factor gramamr 
              
          
        return token # tokens updated from succcesful grammar 
     
    return holder # failed term grammar 



def factor(token):
    "factor grammar check"
    
    holder = token #token for faield grammar 
    
    if token < len(consumedTokens) and consumedTokens[token] == "id": 
      
        token += 1 #if id found consumes token
        return token
    if token < len(consumedTokens) and consumedTokens[token] == "intLiteral":
        token += 1 # if int found consume token
        return token    
    if token < len(consumedTokens) and consumedTokens[token] == "boolLiteral":
        token += 1 # if bool consume token
        return token
    if token < len(consumedTokens) and consumedTokens[token] == "charLiteral":
        token += 1 #if char consume token
        return token
    if token < len(consumedTokens) and consumedTokens[token] == "floatLiteral":
        token += 1 #if float consume token
        return token    
   
    if token < len(consumedTokens) and consumedTokens[token] == "(":
        token += 1
        if token < len(consumedTokens) and expression(token) != token:
            token = expression(token) #updating and consuming token
            if token < len(consumedTokens) and consumedTokens[token] == ")":
                token += 1
                return token            
    
    
    return token # failed token
     

def error(indexToken):
    
    #first error condition
    if indexToken < len(consumedTokens) - 1:
        print("Syntactically Incorrect")
        print("Error invalid Expression beginning at: (" + consumedTokens[indexToken] + ") element #: " + \
        str(indexToken))
    else:
        #second error condition
        print("Incomplete Expression: Expecting More Terms")
    