class UserAnalyzer:
    def __init__(self, users):
        self.users = users

    def filter_users(self):
        return [user for user in self.users if user.get("country") == "Poland"]

    def sum_elements_from_index(self, numbers, start_index, num_elements):
        return sum(numbers[start_index : start_index + num_elements])

    def fill_powers_of_two(self, n):
        return [2**i for i in range(1, n + 1)]

    def analyze(self):
        users = self.filter_users()
        print("Uzytkownicy z Polski:", users)
        numbers = [
            1,
            5,
            2,
            3,
            1,
            4,
            1,
            23,
            12,
            2,
            3,
            1,
            2,
            31,
            23,
            1,
            2,
            3,
            1,
            23,
            1,
            2,
            3,
            123,
        ]
        sum_of_elements = self.sum_elements_from_index(
            numbers, start_index=5, num_elements=10
        )
        print(
            "Suma pierwszych dziesięciu elementów zaczynając od indeksu 5",
            sum_of_elements,
        )

        powers_of_two = self.fill_powers_of_two(20)
        print("Potęgi 2 od 1 do 20", powers_of_two)


def main():

    users = [
        {"name": "Kamil", "country": "Poland"},
        {"name": "John", "country": "USA"},
        {"name": "Yeti", "country": "Poland"},
    ]

    analyzer = UserAnalyzer(users)
    analyzer.analyze()


if __name__ == "__main__":
    main()
