def main(file_Name):
    
    
    # file_Name = input("Please enter the file name: ")
    #global variables 
    global consumedLexemes, consumedTokens, indexToken, symTable, printQueue, printList
    consumedTokens =[]
    consumedLexemes = []
    symTable = {}
    printQueue = {}
    printList = []

    
    #Process the input file and build lists of tokens and lexemes
    file = open(file_Name, "r")
    read_file = file.read()
    List = read_file.split() #bigList is a list of tokens and lexemes (alternating)
    consumedTokens = List[0::2] #List of tokens sliced from bigList (even elements)
    consumedLexemes = List[1::2] #List of lexemes
    
    #runs the program
    indexToken = program()
    
    
    #condition for valid grammar 
    if indexToken == len(consumedTokens) - 1:
        print("Syntactically Correct")
        elem = 0
        while elem < len(printQueue):
            printer(elem)
            elem += 1
    
    
        
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
                        decCheck = declerations(indexToken)
                        if decCheck != indexToken: # runs checks for Declerations
                            indexToken = decCheck
                            stmntCheck = statements(indexToken)
                            if stmntCheck != indexToken: # runs checks fpr Statments
                                indexToken = stmntCheck
                                if consumedTokens[indexToken] == "{": # checks last nessecary element 
                                    indexToken += 1
                                    return indexToken
   
   
   
   
   
    
    return indexToken

   
   
  
    

     
def declerations(token):
    "checks for declration"
     
    check = decleration(token) > token
     
     # while loop to ocmplete decleration checks 
    while token < len(consumedTokens) and check:
        #updates token
        
        holder = decleration(token)
        check = holder > token
        token = holder
    return token
          
def decleration(token):
    
    
    holder = token # holder variable in case of failure
    
    if token < len(consumedTokens) and consumedTokens[token] == "type":
        
        varType = token
        
        token += 1
        if token < len(consumedTokens) and consumedTokens[token] == "id": # checking nessecary tokens and consuming them
            varName = token
            token += 1
            while token < len(consumedTokens) and consumedTokens[token] == "id":
                    # updating the consumed tokens
                    varName = token
                    if consumedLexemes[varName] not in symTable:
                        
                        symTable[consumedLexemes[varName]] = [consumedLexemes[varType], None]
                        
                    else:
                        if consumedLexemes[varName] not in printQueue:
                            
                            printQueue[consumedLexemes[varName]] = ["Error: Variable already Defined", False]
                        
                        else: 
                            
                            printQueue[consumedLexemes[varName]][1] = True
                    
                    
                    token += 1

                       
            
            if token < len(consumedTokens) and consumedTokens[token] == ";":
               # print(consumedLexemes[varName])
                if consumedLexemes[varName] not in symTable:
                    
                    symTable[consumedLexemes[varName]] = [consumedLexemes[varType], None]
                    #print(consumedLexemes[varName]) 
                else:
                    if consumedLexemes[varName] not in printQueue:
                        
                        printList.append(consumedLexemes[varName])                        
                        printQueue[consumedLexemes[varName]] = ["Error: Variable already Defined", True]
                                            
                    else: 
                        printQueue[consumedLexemes[varName]][1] = True
                                        
                    
                    
                token += 1
                
              # valid decleration grammar 
                return token 
    
    else:
        #failed grammar 
        return holder

def statements(token):
    "checks the Statments grammar by callign statment" 
    
    # statements check
    check = statement(token)
    if token < len(consumedTokens) and check:
        holder = statement(token)
        check = holder > token
        token = holder
        
   
    while token < len(consumedTokens) and statement(token) != token:
        #updates token based on statements 
        
        token = statement(token)
       
    return token    
     
def statement(token):
    "Statment Grmamar checks" 
    
    asCheck = assignment(token)
    
    if token < len(consumedTokens) and asCheck != token: # assignment check
        token = asCheck
        return token
    
    
    ifCheck =ifStatement(token)
    
    if token < len(consumedTokens) and ifCheck != token: # if statement check
        token = ifCheck
        return token
    
    
    printCheck = printStmnt(token)
    
    if token < len(consumedTokens) and printCheck != token: # print statement check
        token = printCheck
     
        return token
    
    whileCheck = whileStmnt(token)
    
    if token < len(consumedTokens) and whileCheck != token: # while statement check
        token = whileCheck
        return token
    
    returnCheck = returnStmnt(token)
    
    if token < len(consumedTokens) and returnCheck != token: # return Statement check
        token = returnCheck
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
        expCheck = expression(token)
        if token < len(consumedTokens) and expCheck != token:
            #Updates from expression grammar check 
            token, value = expCheck
            
            if token < len(consumedTokens) and consumedTokens[token] == ";":
                token += 1 # consumes token
                
                if token not in printQueue:
                   
                    printList.append(consumedLexemes[token])
                    printQueue[consumedLexemes[token]] = [value, True]
                
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
            expCheck, value = expression(token)
            
            if token < len(consumedTokens) and expCheck != token:
                token = expCheck # expression grammar check update 
                
                if token < len(consumedTokens) and consumedTokens[token] == ")":
                    token += 1 #consumes token
                
                    stmntCheck = statement(token)
                    if token < len(consumedTokens) and stmntCheck != token:
                      
                        token = stmntCheck # updates tokens
                        
                        check = True
                        
                        state2 = statements(token + 1)
                        if token < len(consumedTokens) and consumedTokens[token] == "else" and state2 != token:
                            
                            token += 1
                            token = state2 # updating token statement 
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
            expCheck, value = expression(token)
            
            if token < len(consumedTokens) and expCheck != token:
                token = expCheck #expression grammar check 
                
                if token < len(consumedTokens) and consumedTokens[token] == ")":
                    token += 1 # consume token
                    stmntCheck = statement(token)
                    
                    if token < len(consumedTokens) and stmntCheck != token:
                        token = stmntCheck # statement grammar check
                        return token

    
    
    return holder

def returnStmnt(token):
    "return Statment check" 
    
    
    holder = token # case of holder 
    
    if token < len(consumedTokens) and consumedTokens[token] == "return":
        token += 1    # consume token 
        if token < len(consumedTokens) and expression(token) != token:
            
            token, value = expression(token) #expression gramamr check 
            
            
            if token < len(consumedTokens) and consumedTokens[token] == ";":
                token += 1 # consume token
                return token
            
     
     
    return holder   # failed grammar check

def assignment(token):
    
    holder = token # case of failed grammar 
    
    if token < len(consumedTokens) and consumedTokens[token] == "id":

        varName = token
        token += 1 # consumign tokens
        if token < len(consumedTokens) and consumedTokens[token] == "assignOp":
            
            token += 1 # consuming token
            start = token
            expCheck, value = expression(token)
            if token < len(consumedTokens) and expCheck != token:
                
                token = expCheck #expression grammar check 
                
                if token < len(consumedTokens) and consumedTokens[token] == ";":
                    token += 1
                    if declared(varName):
                        symTable[consumedLexemes[varName]][1] = value
                            
                    return token #valid grammar!
                  
                  
    return holder# failed Grammar 



     
    
def expression(token):
    "Expression grammar Check"
    holder = token # in case of failed grammar
    
    conCheck, value1  = conjunction(token)
    
    
    if token < len(consumedTokens) and conCheck != token:
        
        token = conCheck #update token consumption
        
        while token < len(consumedTokens) and consumedTokens[token] == "||" and\
        conjunction(token+1) != token + 1:
            
            token += 1
            
            token, value2 = conjunction(token) # optional while loop
            
            value1 = (value1 or value2)
#        
        return token, value1

    
    
    return holder, 0 #failed gramamr 
    
def conjunction(token):
    "conjuction grammar check" 
    
    holder = token # case of failed grammar 
    if token < len(consumedTokens) and equality(token) != token:
        
        token, value1 = equality(token) # equality update. 
        
        if token < len(consumedTokens) and consumedTokens[token] == "&&" and\
        conjunction(token+1) != token + 1:
            
            token += 1
            
            
            token, value2 = conjunction(token)
            
            value1 = (value1 and value2)
            
        return token, value1 # conjuction succcess grammar 
   
     
     
    return holder, 0    # grammar failed
    

def equality(token):
    "equality grammar checks "
    
    check = False # check for optional grammar 
    holder = token
    if token < len(consumedTokens) and relation(token) != token:
        token, value1 = relation(token)
        
        check = True # nessecary grammar met
        
        relCheck, value2 = relation(token + 1)
        
        equOpHold = token
        
        if token < len(consumedTokens) and consumedTokens[token] == "equOp" and relCheck != token + 1:
            
            token += 1
            token = relCheck # token updated
             
            if consumedLexemes[equOpHold] == "==":
                
                
                value1 = (value1 == value2)
                
            else:
                
                value1 = (value1 != value2)
                
                
            return token, value1
    if check:
        return token, value1 # nessecary grammar but not optional
    
    
    return holder,0 # failed grammar 



def relation(token):
    "Relation grammar"
    
    check = False # optional grammar conditional
    holder = token
    
    if token < len(consumedTokens) and addition(token) != token: 
        token, valueInitial = addition(token) #updates token
        
        check = True # nessecary grammar met
        
        
        
        relHolder = token 
        
    
        
        if token < len(consumedTokens) and consumedTokens[token] == "relOp"\
           and token + 1 < len(consumedTokens) and addition(token + 1) != token + 1\
           :
            addCheck, value = addition(token + 1)
        
            token += 1
            if consumedLexemes[relHolder] == "<":
                valueInital = (valueInitial < value)
            elif consumedLexemes[relHolder] == ">":
                valueInital = (valueInitial > value)
            elif consumedLexemes[relHolder] == ">=":
                valueInital = (valueInitial >= value)            
            elif consumedLexemes[relHolder] == "<=":
                valueInital = (valueInitial <= value)    
                
                
            token = addCheck # consuming tokens 
            return token, valueInitial
    
    if check:
        return token, valueInitial # optional grammar met 
     
    return holder, 0 #failed grammar 
        


def addition(token):
    "check for addition grammar"
    
    holder = token
    termCheck, valueInitial  = term(token)
    
    if token < len(consumedTokens) and termCheck != token:
        
        token = termCheck # consuming tokens from term gramamr 
        
        addHolder = token
        
        while token < len(consumedTokens) and consumedTokens[token] == "addOp"\
              and token + 1 < len(consumedTokens) and term(token + 1) != token + 1:
            token += 1
            
            token, value = term(token)
            
            if consumedLexemes[addHolder] == "+":
                valueInitial += value
            else:
                valueInitial -= value
        
        return token, valueInitial # grammar met 
    
    return holder, 0 # gramamr failed 



def term(token):
    "term grammar checks "
    
    holder = token # case of invalid grammar 
    factorCheck, valueInitial = factor(token)
    if token < len(consumedTokens) and factorCheck != token:
        token = factorCheck
        
        lexHolder = token
        
        
        while token < len(consumedTokens) and consumedTokens[token] == "multOp"\
              and token + 1 < len(consumedTokens) and factor(token + 1) != token + 1:
            
            
            
            token += 1  # consume token
            
            token, value = factor(token) # consume tokens from factor gramamr
            
            if consumedLexemes[lexHolder] == "*":
                exponent = 1 
            
            else: 
                exponent = -1
            valueInitial = valueInitial * value ** exponent  
          
        return token, valueInitial
    
    # tokens updated from succcesful grammar 
    return holder, 0 # failed term grammar 



def factor(token):
    "factor grammar check"
    
    holder = token #token for faield grammar 
    
    if token < len(consumedTokens) and consumedTokens[token] == "id": 
        token += 1 #if id found consumes token
        if declared(token - 1):
            
            return token, symTable[consumedLexemes[token-1]][1]
        else:
            return token, 0
    
    if token < len(consumedTokens) and consumedTokens[token] == "intLiteral":
        token += 1 # if int found consume token
        return token, int(consumedLexemes[token-1])    
    
    if token < len(consumedTokens) and consumedTokens[token] == "boolLiteral":
        token += 1 # if bool consume token
        return token, bool(consumedLexemes[token-1])  
    if token < len(consumedTokens) and consumedTokens[token] == "charLiteral":
        token += 1 #if char consume token
        return token, consumedLexemes[token-1]  
    if token < len(consumedTokens) and consumedTokens[token] == "floatLiteral":
        token += 1 #if float consume token
        return token, float(consumedLexemes[token-1])
   
    if token < len(consumedTokens) and consumedTokens[token] == "(":
        token += 1
        expCheck, value = expression(token)
        if token < len(consumedTokens) and expression(token) != token:
            token = expCheck #updating and consuming token
            if token < len(consumedTokens) and consumedTokens[token] == ")":
                token += 1
                return token, value            
    
    
    return token, 0 # failed token
     

def error(indexToken):
    
    #first error condition
    if indexToken < len(consumedTokens) - 1:
        print("Syntactically Incorrect")
        print("Error invalid Expression beginning at: (" + consumedTokens[indexToken] + ") element #: " + \
        str(indexToken))
    else:
        #second error condition
        print("Incomplete Expression: Expecting More Terms")
    
    
def alreadyExists(token):
    if consumedLexemes[token] not in symTable:
        print("Error: Variable already Declared")
        return False
   
   
    else:
        return True
    
def declared(token):
    if consumedLexemes[token] in symTable:
        
        return True
    else:
        
        print("Error: Variable Not declared")
        return False
    

def printer(elem):
    
    set1 = set(printList)
    list1 = list(set1)
    var = list1[elem]
    
    
    if printQueue[var][1]:
        list2 = printQueue.get(list1[elem])
        if type(list2[0]) != int and type(list2[0]) != float and type(list2[0]) != bool:
            print((list2[0]) + ": " + str(var))
        else:
            print(list2[0])
    


main("data.txt")