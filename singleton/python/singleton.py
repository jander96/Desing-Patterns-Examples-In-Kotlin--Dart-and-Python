# Using a class 
class Singleton(object):
    _instance = None
    def __new__(cls):
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls) #If class recive args is more complex
        
        return Singleton._instance


# Using decorator is the best practice in Python
def singleton (cls):
    instances = dict()
    
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap

@singleton
class User(object):
    def __init__(self, username: str) -> None:
        self.username = username

def main():
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()
    instance4 = Singleton()
    
    user1 = User('Jander')
    user2 = User('Gustavo')
    user3 = User('Pepe')
    user4 = User('Lorenzo')
    
    print(instance1)
    print(instance2)
    print(instance3)
    print(instance4)
    print('-----------------------')
    print(user1)
    print(user2)
    print(user3)
    print(user4)
        
if __name__ == '__main__': 
    main()