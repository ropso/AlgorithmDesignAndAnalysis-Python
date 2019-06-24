
class HybridStack():
        def __init__(self,MAX_STACK_SIZE=10):
            self._total_elements=0
            self._stack={}
            self._MAX_STACK_SIZE=MAX_STACK_SIZE
        
        def create_stack(self,value):
            return [value]

        def push(self,value):
            
            stack_no=self._total_elements//self._MAX_STACK_SIZE
            self._total_elements+=1
            if self._stack.get(stack_no)==None:
                #create a new stack and apend the value to it
                self._stack[stack_no]=self.create_stack(value)
            else:
                self._stack[stack_no].append(value)

        def showWorking(self):
            print(self._stack)
        def popHybrid(self):
            if self._total_elements>0:
                self._total_elements-=1
                stack_no=self._total_elements//self._MAX_STACK_SIZE
                value=self._stack[stack_no].pop()
                return value
            else:
                return None


if __name__=="__main__":
    stack=HybridStack(5)
    stack.push(89)
    stack.push(34)
    stack.push(89)
    stack.push(34)
    stack.push(89)
    stack.push(34)
    stack.push(89)
    stack.push(34)
    stack.push(4565)
    stack.push(909)
    stack.push(89)
    stack.push(34)
    stack.push(4565)
    stack.push(909)
    stack.push(89)
    stack.push(34)
    stack.push(4565)
    stack.push(909)
    op=input()
    while (op!="no"):
        poped_elem=stack.popHybrid()
        if poped_elem==None:
            print("stack empty")
            break
        else:
            print(poped_elem,end=" ")
        
        #print("##",stack._total_elements)
    stack.showWorking()