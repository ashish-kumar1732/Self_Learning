class employee:
    price=10
    @classmethod ## use for prioritizing class 
    def show(cls):
        print(f"the price is {cls.price}")

ashish= employee()
ashish.price=50

ashish.show()