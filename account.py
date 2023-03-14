class Account:
    
        def __init__(self, name, amount):
                self.name = name
                self.__balance = amount # 언더바 두 개로 시작하는 속성은 비공개 속성
        
        def __str__(self):
                return "예금주 {}, 잔고 {}".format(self.name, self.__balance)
    
        def withdraw(self, amount):
                self.__balance -= amount
                print("출금 {}원 이후:".format(amount))
                print("\t", self)
            
        def deposit(self, amount):
                self.__balance += amount
                print("입금 {}원 이후:".format(amount))
                print("\t", self)
