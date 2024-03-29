# Python Lab (ITI)

A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

1 - We need to implement a python class that represents the queue data structure.
The class should have these operations:
  - insert(value) => which inserts a new value at the rear of the queue
  - pop() => which returns and removes a value from the front of the queue. We should return None and print a warning message if we tried to pop value from an empty queue
  - is_empty() => which returns True or False to represent whether the queue is empty or not

2 - We need to implement another queue class that has the same properties as previous but with the following changes:
  A. The queue should have a name that is provided as a parameter of its constructor
  B. The queue should have a size that is provided as a parameter of its constructor and if we tried to insert more values than its size raises a custom exception called QueueOutOfRangeException
  C. The queue keeps track with all queues instances that has been created through this class and we can get any queue of them using its name
  D. The queue class should have two class methods called (save, load) which saves all created queues instances to a file and load them when needed. (bonus)

*******************************************************************

3 – Create a new client for weatherapi.com that has the following methods:
  a- get_current_temperature(city)
  b- get_temperature_after(city, days, hour=None)
  c- get_lat_and_long(city)
