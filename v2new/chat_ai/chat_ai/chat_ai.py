import re
question=input("Hi how can i help you")

 


def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text

clean_question= clean_text(question)

words=clean_question.split()

print(words)

found=0


for w in words:
    if found==0:
         #greetings
         if w=="hi":
             print("hi how can i help you")
             found=1
             break
         elif w=="hey":
             print("hi how can i help you")
             found=1
             break
         elif w=="hello":
             found=1
             print("hi how can i help you")
             break

         elif w=="next":
              print("next")
              found=1
              break

         elif w=="intakes":
             print("intakes")
             found=1
             break
         # other
         elif w=="prize" :
             print("which course")
             found=1
             break
         elif w=="much" :
             print("which course")
             found=1
             break

         elif w=="duration":
             print("which course")
             found=1
             break
         elif w=="registration":
             print("registration")
             found=1
             break
         elif w=="register":
             print("registration")
             found=1
             break

         elif w=="payments":
             print("payments")
             found=1
             break
         elif w=="requirements" :
             print("requirements")
             found=1
             break
         elif w=="result" :
             print("requirements")
             found=1
             break

         elif w=="pending" :
             print("pending")
             found=1
             break
    #bsc.management
         elif w=="management":
              print("Management")
              found=1
              break
         elif w=="Manegement":
              print("management")
              found=1
              break
         elif w=="manegment":
              print("management")
              found=1
              break

        #bsc.marketing  
         elif w=="marketing":
              print("marketing")
              found=1
              break
         elif w=="marcketing":
              print("marketing")
              found=1
              break

         elif w=="marceting":
              print("marketing")
              found=1
              break

        #bsc.sf
         elif w=="software":
             print("sf")
             found=1
             break
         elif w=="softeware":
             print("sf")
             found=1
             break
         elif w=="engineering":
             print("sf")
             found=1
             break
         elif w=="enginering":
             print("sf")
             found=1
             break

        #bsc.cs
   
         elif w=="science":
             print("cs")
             found=1
             break
         elif w=="sceince":
             print("cs")
             found=1
             break
             break
         elif w=="computer":
             print("cs")
             found=1
             break

         elif w=="business":
             
             print("business faculty")
             found=1
             break

         elif w=="busines":
            print("business faculty")
            found=1
            break
          
         elif w=="bisness":
             print("business faculty")
             found=1
             break

         elif w=="computing":
             print("computing faculty")
             found=1
             break
         

         elif w=="foundation":
             print("foundation")
             found=1
             break

         
         


             

         #common
         elif w=="courses" :
              for i in words:
                  if i=="business":
                       print("business faculty")
                       found=1
                       break
                  elif i=="busines":
                       print("business faculty")
                       found=1
                       break
                  elif i=="busines":
                       print("business faculty")
                       found=1
                       break

                  elif i=="buissness":
                       print("business faculty")
                       found=1
                       break
                  elif i=="buissness":
                       print("business faculty")
                       found=1
                       break

                  elif i=="computing":
                       print("computing faculty")
                       found=1
                       break

                  elif i=="computer":
                       print("computing faculty")
                       found=1
                       break


                  elif i=="it":
                      print("computing faculty")
                      found=1
                      break
         
                  elif i=="foundation":
                      print("foundation")
                      found=1
                      break
                  else:
                      pass
              print("common")
              found=1
              break




         else:
             pass

if found==0:
    print("sorry i dont get it")
                 
            
                  
           

          
         


          
          
       

       
       




 


   

        

   


        
        
    