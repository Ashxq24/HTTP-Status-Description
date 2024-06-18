import HTTPStatusCodes
response_codes=input("enter the status code of the FTP4 server : ")
if response_codes in HTTPStatusCodes.codes:
   print ("code description: ", HTTPStatusCodes.codes[response_codes])
else:
    print("Sorry , check if the entered status code of the HTTP server is genuine")
