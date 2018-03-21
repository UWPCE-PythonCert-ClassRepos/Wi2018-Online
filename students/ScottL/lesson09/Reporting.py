# ------------Reporting.py ---------------#
# Desc:  class that prints data
# Dev:   Scott Luse
# Date:  03/17/2018
# ChangeLog:(When,Who,What)
# ----------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")

class Reports(object):
    """ Process data using files """

    # --Constructor--
    def __init__(self, id=""):
        # Attributes
        self.id = id

    # --Methods--
    @staticmethod
    def thank_you_printing(name, amount):
        line_divider = "*" * 50
        print(f'''
        {line_divider}
        {name}
        Address

        Dear {name},
        Thank you for your charitable gift of ${amount}.
        {line_divider}
        ''')

    @staticmethod
    def gen_letter_body(name, amount):

        report_text = (f'''Dear {name},

        Thank you for your charitable gift of ${amount}.

                    It will be put to very good use.


                                    Sincerely,
                                            --The Cool Team''')
        return (report_text)
