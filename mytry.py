class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [[0] * self.__cols for _ in range(self.__rows)]

    def book_seats(self, id, seats_to_book):
        if id not in self.__seats:
            print(f"Error: Show with ID {id} not found.")
            return

        for seat in seats_to_book:
            row, col = seat
            if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                if self.__seats[id][row - 1][col - 1] == 0:
                    self.__seats[id][row - 1][col - 1] = 1
                    print(f"Seat booked for Show ID {id} - Row {row}, Column {col}")
                else:
                    print(f"Error: Seat at Row {row}, Column {col} is already booked.")
            else:
                print(f"Error: Invalid seat at Row {row}, Column {col}.")

    def view_show_list(self):
        for show_info in self.__show_list:
            print(f"Show ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"Available seats for Show ID {id}:")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if self.__seats[id][row][col] == 0:
                        print(f"Row {row + 1}, Column {col + 1}: Available")
                    else:
                        print(f"Row {row + 1}, Column {col + 1}: Booked")
        else:
            print(f"Error: Show with ID {id} not found.")


# def main():
    # Create halls and add them to Star_Cinema
hall1 = Hall(3, 4, 1)
hall1 = Hall(3, 4, 1)
hall2 = Hall(4, 5, 2)
Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)

    # Add shows to halls
hall1.entry_show(1, "Movie A", "10:00 AM")
hall1.entry_show(2, "Movie C", "2:00 PM")
hall2.entry_show(3, "Movie B", "1:00 PM")

while True:
        print("\nMenu:")
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hall1.view_show_list()
            hall2.view_show_list()

        elif choice == "2":
            show_id = int(input("Enter the show ID: "))
            hall1.view_available_seats(show_id)
            hall2.view_available_seats(show_id)

        elif choice == "3":
            show_id = int(input("Enter the show ID: "))
            num_tickets = int(input("Enter the number of tickets: "))
            seats_to_book = []
            for _ in range(num_tickets):
                row = int(input("Enter seat row: "))
                col = int(input("Enter seat column: "))
                seats_to_book.append((row, col))
            hall1.book_seats(show_id, seats_to_book)
            hall2.book_seats(show_id, seats_to_book)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()
