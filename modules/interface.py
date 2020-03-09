class Interface(object):
    def Menu(self):
        print("1. a + b\n2. a - b\n3. a * b\n4. a / b\n5.Show Recent Operations\n6.Clear Log\n7.Exponentiang\n8.Find ln(a)\n9.Find Sin(a)\n10.Find Cos(a)\n11.Find Tan(a)\n12.Exit")
    def Select(self):
        option = input()
        option = int(option)
        return option
    def Read(self,number = 2):
        if number == 2:
            a = input()
            b = input()
            a,b = int(a),int(b)
            return a,b
        else:
            a = input()
            a = int(a)
            return a