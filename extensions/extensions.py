



x = input("File name: " )
x = x.strip().lower()
x = x.split('.')
if x[-1]=='bin':
     print("application/octet-stream")
elif  x[-1]=="gif" :
         print("image/gif")

elif  x[-1]=="jpeg" or x[-1]=='jpg':
           print("image/jpeg")

elif x[-1]== "png" :
           print("image/png")

elif x[-1]=='pdf':
     print('application/pdf')
elif x[-1]  =='txt':
            print("text/plain")
elif x[-1]=="zip":
             print("application/zip")
else :
        print ("application/octet-stream")