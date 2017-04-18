__author__ = 'Darcy'
# coding = utf-8


class Hello:

    def __init__(self, name):
        self._name = name

    def sayaHello(self):
        print ("Hello {0}".format(self._name))

man = Hello(name="darcy")
man.sayHello()


class Hi(Hello):

    def __init__(self, name):
        Hello.__init__(self, name)

    def sayHi(self):
        print ("Hi {0}".format(self._name))

newMan = Hi(name="Darcy")
newMan.sayHi()