class Taxi:
    def __init__(self, id, driver_name):
        self.id = id
        self.driver_name = driver_name
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_taxi):
        self.next = next_taxi

class LinkedTaxis:
    def __init__(self):
        self.head = None

    def add_taxi(self, taxi):
        taxi.set_next(self.head)
        self.head = taxi

    def remove_taxi(self, taxi_id):
        current = self.head
        previous = None
        while current is not None and current.id != taxi_id:
            previous = current
            current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def display_taxis(self):
        current = self.head
        while current is not None:
            print(f"Taxi ID: {current.id}, Driver Name: {current.driver_name}")
            current = current.get_next()

# Create a linked list of taxis
taxi_list = LinkedTaxis()

# Create and add 5 taxis to the list
taxi1 = Taxi(1, "Driver A")
taxi2 = Taxi(2, "Driver B")
taxi3 = Taxi(3, "Driver C")
taxi4 = Taxi(4, "Driver D")
taxi5 = Taxi(5, "Driver E")

taxi_list.add_taxi(taxi1)
taxi_list.add_taxi(taxi2)
taxi_list.add_taxi(taxi3)
taxi_list.add_taxi(taxi4)
taxi_list.add_taxi(taxi5)

# Display the taxis in the list
taxi_list.display_taxis()