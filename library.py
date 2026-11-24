from datetime import datetime

FINE_PER_DAY = 2


def parse_date(date_text):
    return datetime.strptime(date_text, "%d-%m-%Y").date()


def days_late(due_date, return_date):
    due = parse_date(due_date)
    returned = parse_date(return_date)
    late_days = (returned - due).days
    return max(late_days, 0)


def is_overdue(due_date, return_date):
    return days_late(due_date, return_date) > 0


def fine(late_days):
    if late_days < 0:
        raise ValueError("Late days cannot be negative")
    return late_days * FINE_PER_DAY


def receipt(due_date, return_date):
    late_days = days_late(due_date, return_date)
    total_fine = fine(late_days)

    return (
        "----- Library Fine Receipt -----\n"
        f"Due date: {due_date}\n"
        f"Return date: {return_date}\n"
        f"Days late: {late_days}\n"
        f"Total fine: Rs. {total_fine}\n"
    )


def main():
    print("===== Library Fine Calculator =====")

    due_date = input("Enter due date (DD-MM-YYYY): ")
    return_date = input("Enter return date (DD-MM-YYYY): ")

    late_days = days_late(due_date, return_date)
    total_fine = fine(late_days)

    print("\n----- Fine Details -----")
    print(f"Due date       : {due_date}")
    print(f"Return date    : {return_date}")
    print(f"Overdue        : {is_overdue(due_date, return_date)}")
    print(f"Days late      : {late_days}")
    print(f"Fine per day   : Rs. {FINE_PER_DAY}")
    print(f"Total fine     : Rs. {total_fine}")
    print()
    print(receipt(due_date, return_date))


if __name__ == "__main__":
    main()