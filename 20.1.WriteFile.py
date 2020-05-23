## "a" ->append->add line after existing line "w"->Override
file=open("student1.txt","w") #access to existing file/if not available create a new file
file.write("\nMohammad Orfat \nAge-42\nAddress: 69th st, woodside\nPhone:64646464646") # "\n-->ensure new line

##we caan also write in a html file (need to know about other file)
file=open("student.html","a")
file.write("\n<h1>This is Header</h1>\n<p>Students name: Sharif</p>")
file.close()

