"""Q2. A school library charges a fine for books returned after the due date acc. To the following condition : -
Days                        	Fine
1-5 days .40 p
6-10 days                   .65p exceeding 6 days
10-15days                  .80p exceeding 10days
15-25days                   1.20p exceeding 15 days
# if the book gets misplaced fine of Rs. 500 on each book, with the due date fine on the day of reporting
# If the book has been hampered Rs.200 on each book, with the due date fine on the day of reporting
# Calculate total fine acc. To the books lend to the student
#Due date to return the book is 25days after the issue date
"""
def calculate_book_fine(days, misplaced=False, hampered=False):
    due_date = 25
    fine = 0

    if misplaced or hampered:
        fine += 500

    if days > due_date:
        days_exceeded = days - due_date

        if days_exceeded <= 5:
            fine += days_exceeded * 0.40
        elif days_exceeded <= 10:
            fine += 5 * 0.40 + (days_exceeded - 5) * 0.65
        elif days_exceeded <= 15:
            fine += 5 * 0.40 + 5 * 0.65 + (days_exceeded - 10) * 0.80
        else:
            fine += 5 * 0.40 + 5 * 0.65 + 5 * 0.80 + (days_exceeded - 15) * 1.20

    return fine


# Example usage:
days_borrowed = 18
is_misplaced = False
is_hampered = False

total_fine = calculate_book_fine(days_borrowed, is_misplaced, is_hampered)
print(f"The total fine for the books is: {total_fine}")
