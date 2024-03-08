# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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


class OrderBookApp:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()
        self.__orderbook.add_order(description, programmer, int(workload))
        print('added!')

    def list_finished_tasks(self):
        orders = self.__orderbook.finished_orders()
        if len(orders) == 0:
            print('no finished tasks')
        else:
            for i in orders:
                print(i)

    def list_unfinished_tasks(self):
        orders = self.__orderbook.unfinished_orders()
        if len(orders) == 0:
            print('no unfinished tasks')
        else:
            for i in orders:
                print(i)

    def mark_task_finished(self):
        id = int(input('id: '))
        self.__orderbook.mark_finished(id)
        print('marked as finished')

    def programmers(self):
        progs = self.__orderbook.programmers()
        if len(progs) == 0:
            print('no programmers')
        else:
            for i in progs:
                print(i)

    def status_programmer(self):
        programmer = input('programmer: ')
        status = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            try:
                if command == "0":
                    break
                elif command == "1":
                    self.add_order()
                elif command == "2":
                    self.list_finished_tasks()
                elif command == "3":
                    self.list_unfinished_tasks()
                elif command == "4":
                    self.mark_task_finished()
                elif command == "5":
                    self.programmers()
                elif command == "6":
                    self.status_programmer()
                else:
                    self.help()
            except:
                print('erroneous input')


# when testing, no code should be outside application except the following:
application = OrderBookApp()
application.execute()
