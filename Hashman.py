class HashMapDemo:

    def __init__(self):
        self.name = [None] * 10
        self.roll = [0] * 10

    def put(self, student_name, roll_no):
        index = roll_no % 10

        self.name[index] = student_name
        self.roll[index] = roll_no

    def display(self):
        for i in range(10):
            if self.name[i] is not None:
                print("Index:", i,
                      "Name:", self.name[i],
                      "Roll No:", self.roll[i])


# Main program
h = HashMapDemo()

h.put("krishna", 41)

h.display()
