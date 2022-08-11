import tkinter as TK
from tkinter import simpledialog
from cgitb import handler
import xml.sax
import xml.etree.ElementTree as ET

mytree = ET.parse('simulation.xml')
myroot = mytree.getroot()


class SimulationHandler(xml.sax.ContentHandler):
   def startElement(self, gridsize, attrs):
      self.current = gridsize
      if  gridsize == "simulation": 
         print(f"-- Simulation {attrs['id']} --")
    
   def characters(self, content):
     if self.current == "gridsize":
       self.gridsize = content
     elif self.current == "cars":
       self.cars = content
     elif self.current == "rsus":
       self.rsus = content
     elif self.current == "speed":
       self.speed = content
     elif self.current == "simtime":
       self.simtime = content
     elif self.current == "probfail":
       self.probfail = content
            
   def endElement(self, gridsize):
    if self.current == "gridsize":
       print(f"Gridsize: {self.gridsize}")
    elif self.current == "cars":
       print(f"Cars: {self.cars}")
    elif self.current == "rsus":
       print(f"Rsus: {self.rsus}")
    elif self.current == "speed":
       print(f"Speed: {self.speed}")
    elif self.current == "simtime":
       print(f"Simtime: {self.simtime}")
    elif self.current == "probfail":
       print(f"% fail: {self.probfail}")
    self.current = ""

def get_value():
   global user_value
   result = simpledialog.askfloat("type a value")
   user_value = result

#tamanho da janela
root = TK.Tk()
root.geometry('1920x1080')

user_value = ''

label = TK.Label(root) 
label.pack()

submitButton = TK.Button(root, text="Start", command=get_value)
submitButton.pack()

def myEntry():
   e = TK.Entry(root, width=10)
   e.pack()
   e.get()

horizontal = TK.Scale(root, from_=0, to=100, orient=TK.HORIZONTAL)
horizontal.pack()
horizontal.get()

def myClick():
    myLabel = TK.Label(root)
    myLabel.pack()

def mySlide():
   myScale = TK.Scale(root, text=horizontal.get())
   myScale.pack()

myButton = TK.Button(root, text="Start", padx=20, pady=20, command=myClick, bg="green")
myButton.pack()

for gridsizes in myroot.iter('gridsize'):
   myButtonGrid = TK.Button(root, text="Type Gridsize", padx=10, pady=10,  command=lambda: [myEntry(), myClick()])
   myButtonGrid.place(x=60, y=10)
   #gridsizes.text = myButtonGrid
   gridsizes.set('newgridsizes', 'yes')

myButtonCars = TK.Button(root, text="Type number of Cars", padx=10, pady=10, command=myClick)
myButtonCars.place(x=60, y=60)

myButtonRsus = TK.Button(root, text="Type number of RSUs", padx=10, pady=10, command=myClick)
myButtonRsus.place(x=60, y=110)

myButtonSpeed = TK.Button(root, text="Type Speed", padx=10, pady=10, command=mySlide)
myButtonSpeed.place(x=60, y=160)

myButtonSimtime = TK.Button(root, text="Type the SimulationTime", padx=10, pady=10, command=myClick)
myButtonSimtime.place(x=60, y=210)

myButtonProb = TK.Button(root, text="Type the %Fail", padx=10, pady=10, command=myClick)
myButtonProb.place(x=60, y=260)

root.mainloop()

#define em qual arquivo os dados inseridos vão
mytree.write('simulation.xml')

handler = SimulationHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('simulation.xml')