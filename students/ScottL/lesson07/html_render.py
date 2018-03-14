# ------------html_render.py Module ---------------#
# Desc:  Classes for html render
# Dev:   Scott Luse
# Date:  03/04/2018
# ChangeLog:(When,Who,What)
# ---------------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

class Element(object):

    # --Fields--
    indent = "    "
    newline = "\n"

    # --Constructor--
    def __init__(self, content = None, tag ="html"):
        # Attributes
        self.list_content = [str(content)] if content else []
        self.cur_tag = tag

    # --Methods--
    def append(self, s):
        self.list_content.append(s)

    def build_content(self, cur_ind):
        str_content = ""
        for item in self.list_content:
            str_content = self.newline.join([str_content, item])
        return str_content

    def output(self, cur_ind=""):
        open_tag = "".join([cur_ind, "<", self.cur_tag, ">"])
        content = self.build_content(cur_ind)
        close_tag = "".join([cur_ind, "</", self.cur_tag, ">"])
        return self.newline.join([open_tag, content, close_tag])

    def render(self, file_out, cur_ind=""):
        file_out.write(self.output(cur_ind))