'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
    <head>
        <meta charset="UTF-8" />
        <title>Python Class Sample page</title>
    </head>
    <body>
        <h2>Python Class - Html rendering example</h2>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text
        </p>
        <hr />
        <ul id="TheList" style="line-height:200%">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
            <li>
                And this is a
                <a href="http://google.com">link</a>
                to google
            </li>
        </ul>
    </body>
</html>
'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()