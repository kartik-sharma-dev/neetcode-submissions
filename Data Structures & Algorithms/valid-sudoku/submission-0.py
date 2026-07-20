class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
                count2 = 0
                new_list = []

                for i in range(len(board)):
                    current_list = []
                    for j in range(len(board)):
                        current_list.append(board[j][count2])
                    
                    new_list.append(current_list)
                    count2 += 1
                a = {}

                count = 0

                for i in board:
                    a[count]=[]
                    for j in i :
                        if j.isdigit():
                            j=int(j)
                            if j in a[count]:
                                return False
                    
                            elif j >= 1 and j <= 9:
                                a[count].append(j)
                        else: 
                            a[count].append(j)
                    count+=1





                b = {}

                count3 = 0

                for i in new_list:
                    b[count3]=[]
                    for j in i :
                        if j.isdigit():
                            j=int(j)
                            if j in b[count3]:
                                return False

                            elif j >= 1 and j <= 9:
                                b[count3].append(j)
                        else: 
                            b[count3].append(j)
                    count3+=1
                    
                blocks=[]
                    
                for i in range(0,len(board),3):

                    for j in range(0,len(board[0]),3):
                        block =  board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3] 
                               
                        
                        blocks.append(block)


                c ={}
                count4 = 0
                

                for i in blocks:
                    c[count4]=[]
                    for j in i :
                        j=str(j)
                        
                        if j.isdigit():
                            j=int(j)
                            if j in c[count4]:
                                return False

                            elif j >= 1 and j <= 9:
                                c[count4].append(j)
                        else: 
                            c[count4].append(j)
                    count4+=1
                    
                return True
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
