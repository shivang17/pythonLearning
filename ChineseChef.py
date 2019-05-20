from Chef_understand_inheritance import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef is able to make the fried rice")

    # you can override any method of the parent class if you want different output, i.e Override them