from os import getenv
from subprocess import call
pwd = getenv("PWD")
try:
	index = open(pwd+"/template.html")
	index.close
	db = open(pwd+"/main-db")
except:
	print("oops")
call("cp "+pwd+"/template.html "+pwd+"/index.html",shell=True)
index = open(pwd+"/index.html","a")
increment=0
for line in db:
	line=line.rstrip()
	line_pieces=line.split("=",2)
	name=line_pieces[0].rstrip()
	increment=increment+1
	call("touch "+str(increment)+".html", shell=True)
	tertiary=open(pwd+"/"+str(increment)+".html", "w")
	tertiary.write("<head><title>"+line_pieces[0]+"</title><link rel='stylesheet' href='main.css'><link href='https://fonts.googleapis.com/css?family=Ubuntu' rel='stylesheet'></head>")
	tertiary.write("<iframe width='560' height='315' src='https://www.youtube.com/embed/videoseries?list="+line_pieces[2]+"' frameborder='0' allowfullscreen></iframe>")
	tertiary.write("<p><a href='file://"+pwd+"/index.html'>Back</a></p>")
	index.write("<p><a href='file://"+pwd+"/"+str(increment)+".html'>"+name+"</a></p>")
index.close()
final=raw_input("Compiled without errors. Cool. Press return to continue. ")
call("chromium-browser --window-size=575x330 --app='file://"+pwd+"/index.html'", shell=True)
