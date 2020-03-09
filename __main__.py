from modules.operations import Operations
from modules.interface import Interface
from modules.storage import Storage
""" Creating objects of interface, calculator and data storage """
Ui = Interface()
Calculator = Operations()
Storage = Storage()
Ui.Menu()
""" Read user command """
command = Ui.Select()
while(command != 12):
    if command == 1: 
        """In this case summarize a and b."""
        a,b = Ui.Read() 
        summ = (Calculator.Summ(a,b))
        print(summ)
        Storage.Write(str(a) +" + " + str(b) + " = " + str(summ) + "\n")
    elif command == 2:
        """In this case find difference between a and b."""
        a,b = Ui.Read()
        diff = (Calculator.Diff(a,b))
        print(diff)
        Storage.Write(str(a) +" - " + str(b) + " = " + str(diff)+ "\n")
    elif command == 3:
        """Find composition a and b."""
        a,b = Ui.Read()
        comp = Calculator.Composition(a,b)
        print(comp)
        Storage.Write(str(a) +" * " + str(b) + " = " + str(comp)+ "\n")
    elif command == 4:
        """Find division between a and b."""
        a,b = Ui.Read()
        div = Calculator.Division(a,b)
        print(div)
        Storage.Write(str(a) +" / " + str(b) + " = " + str(div)+ "\n")
    elif command == 5:
        """Show all operations in this run."""
        Storage.ShowLastOperations()
    elif command == 6:
        """Clear all operations in log.txt."""
        Storage.Clear()
    elif command == 7:
        """a ^ b."""
        a,b = Ui.Read()
        result = Calculator.Expo(a,b)
        print(result)
        Storage.Write(str(a) + " ^ " + str(b) + " = " + str(result) + "\n")
    elif command == 8:
        """Find log(a)"""
        a = Ui.Read(1)
        result = Calculator.Log(a)
        print(result)
        Storage.Write("Ln(" + str(a) +")" + " = " + str(result))
    elif command == 9:
        """Find Sin(a)"""
        a = Ui.Read(1)
        result = Calculator.Sin(a)
        print(result)
        Storage.Write("Sin(" + str(a) +")" + " = " + str(result))
    elif command == 10:
        """Find Cos(a)"""
        a = Ui.Read(1)
        result = Calculator.Cos(a)
        print(result)
        Storage.Write("Cos(" + str(a) +")" + " = " + str(result))
    elif command == 11:
        """Find Tan(a)"""
        a = Ui.Read(1)
        result = Calculator.Tan(a)
        print(result)
        Storage.Write("Tan(" + str(a) +")" + " = " + str(result))        
    else:
        print("Uknown Option")

    command = Ui.Select()
Storage.Close()
