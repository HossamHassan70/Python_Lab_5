class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: Cannot pop value from an empty queue")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


class QueueOutOfRangeException(Exception):
    pass


class QueueWithProperties(Queue):
    queue_instances = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.__class__.queue_instances[name] = self

    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException("Queue size exceeded")
        super().insert(value)

    @classmethod
    def get_queue(cls, name):
        return cls.queue_instances.get(name)

    @classmethod
    def save(cls, filename):
        queue_data = []
        for queue in cls.queue_instances.values():
            queue_data.append(
                {"name": queue.name, "size": queue.size, "queue": queue.queue}
            )
        with open(filename, "w") as file:
            file.write(str(queue_data))

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            queue_data = eval(file.read())
        for data in queue_data:
            name = data["name"]
            size = data["size"]
            queue = QueueWithProperties(name, size)
            queue.queue = data["queue"]


my_queue = Queue()

my_queue.insert(10)
my_queue.insert(20)
my_queue.insert(30)


print("Is the queue empty?", my_queue.is_empty())  # Output: False

value_popped = my_queue.pop()
print("Popped value:", value_popped)  # Output: Popped value: 10

print("Is the queue empty?", my_queue.is_empty())  # Output: False

empty_queue = Queue()
value_popped_empty = empty_queue.pop()
