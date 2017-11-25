class CircularBufferException(Exception):
    pass


class BufferFullException(CircularBufferException):
    pass


class BufferEmptyException(CircularBufferException):
    pass


class CircularBuffer_Mine():
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.write_pos = 0
        self.read_pos = 0
        self.empty = True
        self.full = False
        
    def inc_write_pos(self):
        self.write_pos += 1
        if self.write_pos == self.capacity:
            self.write_pos = 0
            
    def inc_read_pos(self):
        self.read_pos += 1
        if self.read_pos == self.capacity:
            self.read_pos = 0
        
    def write(self, val, protected=True):
        if protected and self.full:
            raise BufferFullException
        self.buffer[self.write_pos] = val
        self.inc_write_pos()
        self.empty = False
        if self.write_pos == self.read_pos and not self.empty:
            self.full = True
    
    def overwrite(self, val):
        if self.full:
            self.inc_read_pos()
            self.write(val, protected=False)
        else:
            self.write(val)

    def read(self):
        if self.empty:
            raise BufferEmptyException
        val = self.buffer[self.read_pos]
        self.buffer[self.read_pos] = None
        self.inc_read_pos()
        self.full = False
        if set(self.buffer) == {None}:
            self.empty = True
        return val
     
    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_pos = self.write_pos
        self.empty = True
        self.full = False


class CircularBuffer():
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        
    def write(self, val):
        if len(self.buffer) == self.capacity:
            raise BufferFullException
        self.buffer.append(val)
    
    def overwrite(self, val):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(val)

    def read(self):
        if self.buffer == []:
            raise BufferEmptyException
        return self.buffer.pop(0)
     
    def clear(self):
        self.buffer = []