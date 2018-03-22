#!/usr/bin/python
"""
Lesson 7: HTML rendering from py
"""


class Element:
    """Class: Element() initializes Element.content as a list"""
    tag = "html"
    ind_lvl = 0

    def __init__(self, content = None):
        try:
            self.content.append(content)
        except AttributeError:
            self.content = []
            if content is not None:
                self.content.append(content)

    def append(self, args):
        """Element.append(string) stores string"""
        self.content.append(args)

    def render(self, out_file, cur_ind=""):
        """Element.render(open_file_seed, cur_ind = "") takes a open_file and
            write HTML code to it with an indentation format of cur_ind = ""
            ie: no indentation"""
        # open <tag>
        out_file.write(cur_ind * self.ind_lvl + "<" + self.tag + ">\n")
        print(self.tag)
        print(range(len(self.content)))
        for i in range(len(self.content)):
            print(i)
            try:
                self.content[i].content
            except AttributeError:
                # current class does not have a self.content attribute, print out content
                out_file.write(cur_ind * (self.ind_lvl + 1) + self.content[i] + "\n")
            else:
                # go down a lvl in class
                # eval() takes a expression, evaluates the output as an object
                self.content[i].render(out_file, cur_ind)
        out_file.write(cur_ind * self.ind_lvl + "</" + self.tag + ">\n")
        print("returned from ", self.tag)
        return






class Html(Element):
    tag = "Html"
    ind_lvl = 0


class Body(Element):
    tag = "Body"
    ind_lvl = 1


class P(Element):
    tag = "P"
    ind_lvl = 2


class Head(Element):
    tag = "Head"
    ind_lvl = 1


class Title(Element):
    tag = "Title"
    ind_lvl = 2
