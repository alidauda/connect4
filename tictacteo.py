
def TicTac(field):
    for row in range(13):
        if row%2==0:
            parRow=int(row/2)
            for column in range(13):
                if column%2==0:
                    parColumn=int(column/2)
                    if column!=12:
                        print(field[parColumn][parRow],end="")
                    else:
                        print(field[parColumn][parRow])
                else:
                    print("|",end="")
        else:
            print("------------")

Player=1
CurrentField=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
TicTac(CurrentField)
while(True):
    print('your turn: ',Player)
    MoveRow=int(input("please enter the row: "))
    MoveColumn=int(input("please enter a column: "))
    if Player==1:
        #move for player 1
        if CurrentField[MoveColumn][MoveRow]==" ":
            CurrentField[MoveColumn][MoveRow]="x"
            print("row used")
        Player=2
    else:
        #move for player 2
        if CurrentField[MoveColumn][MoveRow]==" ":
            CurrentField[MoveColumn][MoveRow]="O"
        Player=1
    
    TicTac(CurrentField)
print(TicTac())    
    
