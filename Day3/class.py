#class in python

class student:
            #constructor is a function of class which is called immediately after creating object (automatically)
            def __init__(self,student_name,usn_no,course):
                    self.student_name=student_name
                    self.usn_no=usn_no
                    self.course=course
            def print_details(self):
                    print(f'''name={self.student_name} usn_no= {self.course}''')

# Vishal=student("Vishal",1234,"python")
# shivam=student("shivam",6749557,"Javascript")                   
# sahil=student("sahil",5367754,'java')

# Vishal.print_details()
# shivam.print_details()
# sahil.print_details()



 #def add(a, b=5): return a + b; print(add(3))



class laptop(student):
       
             def __init__(self, student_name,usn_no , course,cpu,gpu,ram):
                super().__init__(student_name,usn_no, course)
                self.cpu=cpu
                self.gpu=gpu
                self.ram=ram
             def print_details(self):
                     print(f"CPU={self.cpu} GPU={self.gpu} ram={self.ram}")    
                     return super().print_details()



                        


                













                
       