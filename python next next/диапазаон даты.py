class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other: 'Date') -> bool:
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def __gt__(self, other: 'Date') -> bool:
        return other < self

    def __eq__(self, other: 'Date') -> bool:
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def is_between(self, start: 'Date', end: 'Date') -> bool:
        return start < self < end

def read_date() -> Date:
    date_str = input()
    day, month, year = map(int, date_str.split('.'))
    return Date(day, month, year)

def main() -> None:

    date1 = read_date()
    date2 = read_date()
    date3 = read_date()

    if date1 > date2:
        date1, date2 = date2, date1

    if date3.is_between(date1, date2):
        print("YES")
        
    else:
        print("NO")

if __name__ == "__main__":
    main()