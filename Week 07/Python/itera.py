class CustomIter:
    def __init__(self,data) -> None:
        self.__data = data
        self.__index = 0
        self.__length = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__index < self.__length:
            val =  self.__data[self.__index]
            self.__index+=2
            return val
        else:
            raise StopIteration
        
custom_iter = CustomIter('Python Programming')
print(next(custom_iter))
print(next(custom_iter))
print(next(custom_iter))