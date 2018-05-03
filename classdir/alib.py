# py
class IPPULL:
   message = "http://ipinfo.io"

   @classmethod
   def cfoo(cls):
      print(cls.message)

   def foo(self, msg):
      self.message = msg
      print(self.message)

   def __str__(self):
      return self.message

   def __init__(self, color):
     self.color = color
   def changeColor(self):
     print(self.color)
