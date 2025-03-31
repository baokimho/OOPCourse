class Task:
    id = 1 
    def __init__(self, description, programmer, workload):
        self.id = Task.id 
        Task.id += 1
        self.description = description
        self.workload = workload 
        self.programmer = programmer
        self.finished = False
    
    def mark_finished(self):
        self.finished = True
    
    def is_finished(self):
        return self.finished
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.finished else 'NOT FINISHED'}"


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.orders.append(task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        programmer_set = set()
        for order in self.orders:
            programmer_set.add(order.programmer)
        return list(programmer_set)
    
    def mark_finished(self, id: int):
        found = False
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                found = True
                break
        if not found:
            raise ValueError(f"No task with id {id} found")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished = 0
        unfinished = 0
        finished_w = 0
        unfinished_w = 0
        found = False
        for order in self.orders:
            if order.programmer == programmer:
                found = True
                if order.is_finished():
                    finished += 1
                    finished_w += order.workload
                else:
                    unfinished += 1
                    unfinished_w += order.workload
        
        if not found:
            raise ValueError(f"The programmer name {programmer} is not found")

        return (finished, unfinished, finished_w, unfinished_w)

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def help(self):
        print("\ncommands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        while True:
            self.help()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    description = input("description: ")
                    programmer_workload = input("programmer and workload estimate: ").strip()
                    programmer, workload = programmer_workload.rsplit(" ", 1)
                    workload = int(workload)
                    self.__orderbook.add_order(description, programmer, workload)
                    print("added!")
                except ValueError:
                    print("erroneous input")
                except IndexError:
                    print("erroneous input")
            elif command == "2":
                finished = self.__orderbook.finished_orders()
                if not finished:
                    print("no finished tasks")
                else:
                    for task in finished:
                        print(task)
            elif command == "3":
                unfinished = self.__orderbook.unfinished_orders()
                if not unfinished:
                    print("no unfinished tasks")
                else:
                    for task in unfinished:
                        print(task)
            elif command == "4":
                try:
                    task_id = int(input("Enter task ID to mark as finished: "))
                    self.__orderbook.mark_finished(task_id)
                    print(f"Task {task_id} marked as finished.")
                except ValueError:
                    print("erroneous input")
            elif command == "5":
                programmers = self.__orderbook.programmers()
                if not programmers:
                    print("No programmers found.")
                else:
                    for programmer in programmers:
                        print(programmer)
            elif command == "6":
                try:
                    programmer_name = input("Enter programmer name: ")
                    status = self.__orderbook.status_of_programmer(programmer_name)
                    print(f"Finished tasks: {status[0]}, Unfinished tasks: {status[1]}, Finished hours: {status[2]}, Unfinished hours: {status[3]}")
                except ValueError:
                    print("erroneous input")
            else:
                print("Invalid command.")


#PART 1
# Example usage:
# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())

# t2 = Task("program webstore", "Adele", 10)
# print(t2)

# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t3)
#PART 2
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# for order in orders.all_orders():
#     print(order)

# print()  # Print an empty line

# for programmer in orders.programmers():
#     print(programmer)

# my_list = [1, 1, 3, 6, 4, 1, 3]
# my_list2 = list(set(my_list))
# print(my_list)
# print(my_list2)

#PART 3
# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Eric", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)

# orders.mark_finished(1)
# orders.mark_finished(2)

# for order in orders.all_orders():
#     print(order)

#Part 4 
# orders = OrderBook()  
# orders.add_order("program webstore", "Adele", 10 ) 
# orders.add_order("program mobile app for workload accounting", "Adele", 25) 
# orders.add_order("program app for practising mathematics", "Adele", 100 ) 
# orders.add_order("program the next facebook", "Eric", 1000) 
# orders.mark_finished(1) 
# orders.mark_finished(2) 
# status = orders.status_of_programmer("Adele") 
# print(status) 

#Part 1 application
app = OrderBookApplication()
app.execute()