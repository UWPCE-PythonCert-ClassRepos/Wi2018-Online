contents = '''     '''


class pagedesign:

     def phead():

         file = open("page1.html",'a+')
         file.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN \" >")
         file.write("\n")
         file.write("<html>")
         file.write("\n")
         file.write("     <head>")
         file.write("\n")
         file.write("         <meta charset = \"UTF-8 \"/>")
         file.write("\n")
         file.write("         <title> Python Class Sample  page </title>")
         file.write("\n")
         file.write("    </head>")
         file.write("\n")
         file.write("    <body>")
         file.write("\n")
         file.write("        <h2>Python Class - Html rendering example</h2>")
         file.write("\n")
         file.write("        <p style = \"text-align: center; font-style: oblique;\" >")
         file.write("\n")
         file.write("               Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text")
         file.write("\n")
         file.write("        </p>")
         file.write("\n")
         file.close()

     def body():

         file = open("page1.html",'a')
         file.write("       <hr/>")
         file.write("\n")
         #file.write("             ul id=\"TheList\" style=\"line-height:200%\">")
         file.write("\n")
         file.write("               <li>")
         file.write("\n")
         file.write("                    The First item in the list ")
         file.write("\n")
         #file.write("               <\li>")
         file.write("\n")
         file.write("               <li style = \"color: red \">")
         file.write("\n")
         file.write("                   This is the second item")
         file.write("\n")
         file.write("               </li>")
         file.write("\n")
         file.write("               <li>")
         file.write("\n")
         file.write("                And this is a <a href=\"http://google.com\">link</a> to google")
         file.write("\n")
         #file.write("               <\li>")
         file.write("   </body>")
         file.write("\n")
         file.write("</html>")
         file.close()

a1= pagedesign
a2 = pagedesign
a1.phead()
a2.body()


def main():
             browseLocal(contents)


def browseLocal(webpageText, filename='page1.html'):
             '''Start your webbrowser on a local file containing the text
             with given filename.'''
             import webbrowser, os.path
             webbrowser.open("file:///" + os.path.abspath(filename))  # elaborated for Mac

main()