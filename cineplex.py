class Star_cinema:
    __hall_list=[]

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self, rows,cols, hall_no) -> None:
        super().__init__()
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]

    def entry_show(self, id, movie_name, time):
        show_info=(id, movie_name, time)
        self.show_list.append(show_info)
        # self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

        self.seats[id] = []
        for j in range(self.rows):
            row = []
            for i in range(self.cols):
                row.append(0)
            self.seats[id].append(row)

    def book_seats(self, id, seatList):
        if id not in self.seats:
            print(f"Error : show id: {id} is not found")

        for seat in seatList:
            row, col=seat
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if self.seats[id][row-1][col-1]==0:
                    self.seats[id][row-1][col-1]=1
                    print(f"Booked for Id: {id}, seat no, row:{row},col:{col}")
                else:
                    print(f"Sorry, seat {row},{col} is booked")
            else:
                print(f"invalid row column {row},{col}")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show id. {show[0]}, Movie: {show[1]}, time: {show[2]}")

    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show Id: {id}")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col]==0:
                        print(f"Row: {row+1}, col: {col+1}: Available")
                    else:
                        print(f"Row: {row+1}, col: {col+1}: Booked")
        else:
            print(f"Error: {id} id not found")




hall1=Hall(5, 5, 1)
hall1=Hall(5, 5, 2)

Star_cinema.entry_hall(hall1)

hall1.entry_show(1, "RRR", "12:00 PM")
hall1.entry_show(2, "SSS", "3:00 PM")

while True:
    print("\nMenu:")
    print("Option 1: View Show List")
    print("Option 2: Available seats")
    print("Option 3: Book seats")
    print("Option 4: Exit")

    chose=input("Chose a Option: ")

    if chose=="1":
        hall1.view_show_list()

    elif chose == "2":
        showId= int(input("enter Id: "))
        hall1.view_available_seats(showId)

    elif chose=="3":
        showId=int(input("enter showId: "))
        nm_tickets=int(input("Enter no. of tickets: "))
        seats_to_book=[]
        for single in range(nm_tickets):
            row=int(input("Enter row no. "))
            col=int(input("Enter column no. "))
            seats_to_book.append((row,col))
        hall1.book_seats(showId, seats_to_book)

    elif chose=="4":
        break

    else:
        print("Invalid choosing. Choose option correctly")