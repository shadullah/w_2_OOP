def double_decker():
    print('starting double decker')
    def inner_fun():
        print("inside the inner")
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_som(work):
    print("work started")
    work()
    print("work ended")

# do_som(2)
# do_som('ami busy')

def coding():
    print('coding inpython')

do_som(coding)
