H,M = map(int,input().split())
cook = int(input())
0 <= H <= 23
0 <= M <= 59
0 <= cook <= 1000

if M + cook <= 59 :             
   M = M + cook
else :
  total = M + cook              
  h = total // 60               
  H = H + h                     
  M = total % 60                
  H = H % 24                    
      
  
print(H,M)