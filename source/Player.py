



class Player:
    """
#########################################################
##  IA for Tic Tac Toe game                            ##
#########################################################
    

"""
    def __init__(self,pnum,turn =True):
        self.pnum=pnum
        self.values=[0,0,0,0,0,0,0,0,0]
        self.turn=turn
    def heuristic(self,value):
        points=0
        for i in range(3):
            points+=self.same([self.values[i*3],self.values[3*i +1],self.values[3*i +2]],value)
            points+=self.same([self.values[i],self.values[i+3],self.values[i+6]],value)
        for i in range(2):
            points+= self.same([self.values[i*2],self.values[4],self.values[8-i*2]],value)
        return points            
                    
                            
                              
            
    def same(self,lista,value = None):
        same=True
        count = 3
        for i in lista:
            if(value==None):
                value=i
            if(i != value):
                if(i !=0):
                    return False
                same =False
                count -= 1
        start=lista[0]
        end= lista[2]
        return True + same* 6 + count
    def act(self,game):
      if(self.turn):
        pos=self.play(game.values,3,self.pnum - 1)[1]
        
        if(pos == -1):
            return 0
        zeros=[i for i in range(len(game.values)) if(game.values[i]==0)]
        if(self.pnum==1):
            game.setX(zeros[pos])
            self.turn= False
            print "X",zeros[pos]
            return 1
        else:
            game.setO(zeros[pos])
            print "O",zeros[pos]
            self.turn=False
            
            return 1
        return 0
         
    def play(self,values,depth,MAX=True):
     
      if(self.turn):
        lista=values
        zeros=[i for i in range(len(lista)) if(lista[i]==0)]
        if(depth ==0 or zeros ==[] ):
            return (self.heuristic(2)- self.heuristic(1),-1)
        self.values=[]
        for i in values:
            self.values.append(i)
        print zeros
        reserved=[i for i in range(len(lista)) if(lista[i]!=0)]
        
        if(MAX):
            m= -100
        else:
            m= 100                     
        result=-1                       
        for i in range(len(zeros)):
            self.lista=[]
            for j in values:
                self.lista.append(j)
            k=zeros[i]
            lista_values=list(values)
            lista_values[k]=MAX +1
            val=self.play(lista_values,depth-1,not MAX)
            if( MAX):
                if(val[0] >= m):
                    m= val[0]
                    result=i
            else:
                if(val[0]<= m):
                    
                    m= val[0]
                    result= i
            print (MAX,m,zeros[result])
        return (m,result)
                        
                    
        

