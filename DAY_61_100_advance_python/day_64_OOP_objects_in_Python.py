class Job:
   name: None
   salary: None
   hours: None

   def __init__(self, name, salary, hours):
     self.name = name
     self.salary = salary
     self.hours = hours

   def print(self):
     print("=== JOB ===")
     print()
     print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}")


class doctor(Job):
  experience: None
  speciality: None

  def __init__(self, salary, hours, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.experience = experience

  def print(self):
    print("=== JOB ===")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(Job):
    subject: None
    position: None

    def __init__(self, salary, hours, subject, position):
     self.name = "Teacher"
     self.salary = salary
     self.hours = hours
     self.subject = subject
     self.position = position

    def print(self):
     print("=== JOB ===")
     print()
     print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}")
     print(f"{self.subject:<10} {self.position:>21}")

lawyer = Job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("Pediatric Consultant", "$120,000", "48", "7")
doc.print()

teach = teacher("660K", "30HRS", "Asst. Principal", "Computer Science")
teach.print()




