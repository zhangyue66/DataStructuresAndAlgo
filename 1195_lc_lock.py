from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.l1 = Lock()
        self.l2 = Lock()
        self.l3 = Lock()
        self.l4 = Lock()
        self.l1.acquire()
        self.l2.acquire()
        self.l3.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n//3 - self.n//15):
            self.l1.acquire()
            printFizz()
            
            self.l4.release()

                       	
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//5 - self.n // 15):
            self.l2.acquire()
            printBuzz()
            self.l4.release()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n // 15):
            self.l3.acquire()
            printFizzBuzz()
            self.l4.release()
            


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:       
        for i in range(1,self.n+1):
            self.l4.acquire()
            if i % 15 == 0:
                self.l3.release()
            elif i % 3 ==0:
                self.l1.release()
            elif i % 5 == 0:
                self.l2.release()

            else:
                printNumber(i)
                self.l4.release()
                
        
