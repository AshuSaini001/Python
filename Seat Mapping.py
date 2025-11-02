# Function to load seat data from a text file
def load_seats(filename="seats.txt"):
    # Open the file in read mode and parse each line into a list of integers
    with open("F:/LPU/Python/Project/seat.txt", "r") as f:
        return [list(map(int, line.strip().split())) for line in f]

# Function to save updated seat data back to the text file
def save_seats(seats, filename="seats.txt"):
    # Open the file in write mode and write each row as space-separated values
    with open("F:/LPU/Python/Project/seat.txt", "w") as f:
        for row in seats:
            f.write(" ".join(map(str, row)) + "\n")

# Function to display the seat map visually in the console
def display_seats(seats):
    print("\nSeat Map:")
    # Use 🟩 for vacant (0) and 🟥 for occupied (1)
    for row in seats:
        print(" ".join(["🟩" if s == 0 else "🟥" for s in row]))
    print()

# Function to update the status of a specific seat
def update_seat(seats, row, col, status):
    # Check if the given row and column are within valid range
    if 0 <= row < len(seats) and 0 <= col < len(seats[0]):
        seats[row][col] = status  # Update the seat status
    else:
        print("Invalid seat position!")  # Handle out-of-bound input

# Function to count total occupied and vacant seats
def count_seats(seats):
    total = sum(row.count(1) for row in seats)   # Count occupied seats
    vacant = sum(row.count(0) for row in seats)  # Count vacant seats
    return total, vacant

# Main function to run the seat occupancy program
def main():
    seats = load_seats()  # Load initial seat data

    while True:
        display_seats(seats)  # Show current seat map
        print("Options:")
        print("1. Mark seat")     # Option to update seat status
        print("2. Count seats")   # Option to count seats
        print("3. Exit")          # Option to quit the program

        choice = input("Enter choice: ")  # Get user input

        if choice == "1":
            # Get seat position and status from user
            r = int(input("Row: "))
            c = int(input("Column: "))
            s = int(input("Status (1=Occupied, 0=Vacant): "))
            update_seat(seats, r, c, s)  # Update seat
            save_seats(seats)            # Save changes to file

        elif choice == "2":
            # Count and display seat statistics
            occ, vac = count_seats(seats)
            print(f"Occupied: {occ}, Vacant: {vac}")

        elif choice == "3":
            break  # Exit the loop and end the program

        else:
            print("Invalid choice!")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()
