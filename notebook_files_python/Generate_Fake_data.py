from faker import Faker
import random

# create a employee database using python
# 1) Employee_name
# 2) Salary (20000 - 200000)
# 3) Employee_Designantion -  ['Intern', 'Junior dev', 'Senior dev', 'Manager', 'Sr manager','Product manager']
# 4) Ph_no (10 digits 6-9) (8618042684)
# 5) city
# 6) nationality
# 8) Email
# 9) company_name

fake = Faker()

Name = []
Salary = []
Employee_Designantion = []
Ph_no = []
city = [] 
Nationality = [] 
Email = [] 
company_name = [] 

for i in range(10):
    Name.append(fake.name())
    Salary.append(random.randint(20000, 200000))
    Employee_Designantion.append(random.choice(['Intern', 'Junior dev', 'Senior dev', 'Manager', 'Sr manager','Product manager']))
    Ph_no.append(random.randint(6000000000,9999999999 ))
    city.append(fake.city())
    Email.append(fake.email())
    company_name.append(fake.company())


for i in range(10):
    print(f'Name: {Name[i]}')
    print(f'Employee Designantion: {Employee_Designantion[i]}')
    print(f'Email: {Email[i]}')
    print(f'company_name: {company_name[i]}')
    print(f'Phone No: {Ph_no[i]}')
    print(f'Salary: {Salary[i]}')
    print(f'city: {city[i]}')
    print("*"*100)

