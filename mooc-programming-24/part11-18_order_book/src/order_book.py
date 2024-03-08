# Write your solution here:
from random import randint as ri
class Task:
    ids = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.ids
        Task.ids += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._is_finished = False

    def is_finished(self):
        return self._is_finished

    def mark_finished(self):
        self._is_finished = True

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.is_finished() else 'NOT FINISHED'}"
    

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([i.programmer for i in self.all_orders()]))

    def mark_finished(self, id: int):
        search = [i for i in self.all_orders() if i.id == id]
        if len(search) == 0:
            raise ValueError('Task not found')
        search[0].mark_finished()
    
    def finished_orders(self):
        return [i for i in self.all_orders() if i.is_finished()]

    def unfinished_orders(self):
        return [i for i in self.all_orders() if not i.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError('Programmer not found')
        tasks = [i for i in self.all_orders() if i.programmer == programmer]
        finished = [i.workload for i in tasks if i.is_finished()]
        unfinished = [i.workload for i in tasks if not i.is_finished()]
        return (len(finished), len(unfinished), sum(finished), sum(unfinished))


if __name__ == "__main__":
    # #Part 1
    # t1 = Task("program hello world", "Eric", 3)
    # print(t1.id, t1.description, t1.programmer, t1.workload)
    # print(t1)
    # print(t1.is_finished())
    # t1.mark_finished()
    # print(t1)
    # print(t1.is_finished())
    # t2 = Task("program webstore", "Adele", 10)
    # t3 = Task("program mobile app for workload accounting", "Eric", 25)
    # print(t2)
    # print(t3)

    # #Part2
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # for order in orders.all_orders():
    #     print(order)

    # print()

    # for programmer in orders.programmers():
    #     print(programmer)

    # # #Part 3
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Eric", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # for order in orders.all_orders():
    #     print(order)

    # Part4
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
