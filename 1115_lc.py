from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        #self.foo_lock.acquire()
        self.bar_lock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            #with self.bar_lock:
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            #with self.foo_lock:
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
