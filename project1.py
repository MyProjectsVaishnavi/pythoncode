from login import invaliduser
class User:
     user1=[{'user_id':1234,'user_name':'Bindhu','Designation':'Employee Manager','Request':'Permission','DateOfSubmit':'10-10-2017'},{'user_id':1235,'user_name':'Anu','Designation':'Private Employee','Request':'Sign','DateOfSubmit':'20-09-2017'}]
     def insertuser(user1): 
          user={}
          print("Enter the User details to insert ")
          user['user_id']=input("Enter the user id  :")
          user['user_name']=input("Enter the user name  :")
          user['Designation']=input("Enter the Designation    :")
          user['Request']=input("Enter the Request:")
          user['DateOfSubmit']=input("Enter the DateOfSubmit :")
          user1.append(user)
          print(user1)
     def updateuser(user1):
         key=input("Enter the key to search:")
         pos=int(input("Enter the list position:"))
         user1[pos][key]=input("Enter the update:")
         print(user1)

     def deleteuser(user1):
         pos=int(input("Enter the list position:"))
         user1.remove(user1[pos])
         print(user1)

     def viewuser(user1):
         print('#'*70)
         print("ID\tNAME\t\tDESIGNATION\t\tREQUEST\tDATEOFSUBMIT")
         print('#'*70)
         for i in user1:
               print(str(i['user_id'])+'\t'+str(i['user_name'])+'\t\t'+str(i['Designation'])+'\t '+str(i['Request'])+'\t '+str(i['DateOfSubmit']))
         print('#'*70)
     while(True): 
               print("1.Insert\n2.Update\n3.Delete\n4.List")
               choice=int(input("Enter Your choice:"))
               if(choice==1):
                    insertuser(user1)
               if(choice==2):
                    updateuser(user1)
               if(choice==3):
                    deleteuser(user1)
               if(choice==4):
                    viewuser(user1)
               else:
                    print("Enter Correct choice:")
f1=open("file.txt","w")
f1.write(user1)
f1.close()
f1=open("file.txt","r")
print(f1)
f1.close()
ob1=User1()
