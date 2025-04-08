def isSafe(mat,row,col):
	if(row==0):
		return True;
	for i in range(row-1,-1,-1):
		if(mat[i][col]==1):
			return False;
	for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):

		if(mat[i][j]==1):
			return False; 
	for i,j in zip(range(row-1,-1,-1),range(col+1,4,1)):
		if(mat[i][j]==1):
			return False;
			
	return True;
def solveQueen(row,mat,n):
	if(row==4):
		
	
		for i in range(len(mat)):
			for j in range(len(mat[0])):

				print(mat[i][j],end=" ")
			print("\n");
		return True;


	for col in range(4):
		if isSafe(mat,row,col):
			mat[row][col]=1;
			if(solveQueen(row+1,mat,n)):
				return True;
			mat[row][col]=0;
	return False	
	
if __name__ == '__main__':

	 mat=[[0 for _ in range(4)] for _ in range(4)]
		
	 solveQueen(0,mat,4)
