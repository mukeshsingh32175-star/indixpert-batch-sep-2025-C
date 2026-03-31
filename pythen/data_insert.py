# student registration
#view the student record
#serch th student record
#listdata=[]

#for i in range  (1,3):  
 #data={
 #      "id ":int(input ("enter your id :")),
  
  #     "name" :input("enter your name: ")     
  
  #    }


#listdata.append(data)
#print(listdata)
listdata=[]
def student_registration():
      print("***registration***")
      #listdata=[]
      stud_number=int(input("how many student you want to resgister"))
      for n in range(stud_number) :
       student_data={}
       student_data["id"]=int(input("enter the student id: "))
       student_data["name"]=input("enter the student name: ")
       student_data["email"]=input("enter the student email: ")
       student_data["address"]=input("enter your address: ")
       listdata.append(student_data)
       print("***registration_sucessful***")
       
       
       
       
      
def vew_student_record():
     print(listdata)
                
                
def search_student_record():
      user_input=int(input("enter the student id : "))
      for d in listdata:
            if user_input==d["id"]:
                  print("****record_found***")
                  print(d)
            
          
                  
            
            
def menu():
      while True:
            print("***MENU***")
            print("1.student registration")
            print("2.view the student record")
            print("3.search the student record")
            print("4.exit..")
            user_choice=int(input("enter your choice: ")) 
            
            if user_choice==1:
               
                  student_registration()
                  continue
            elif user_choice==2:
                  
                  vew_student_record()
                  continue
            elif user_choice==3:
                 
                  search_student_record()
                  continue
            elif user_choice == 4:
                  break
            else:
                  print("plese enter the valid choice...!") 
                  continue             


menu()            
        
        
        
        
        
                             