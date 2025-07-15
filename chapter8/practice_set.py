## class- "Programmer" 


class programmer:
    company="Microsoft"
    def __init__(self,name, salary, pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
        
ashish=programmer("ashish",125000,303012)

print(ashish.salary,ashish.company)

nitesh=programmer("nitesh",12500,303016)
print(nitesh.pincode, nitesh.company)


###