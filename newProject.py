class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_mean(self, lst):
        return sum(lst) / len(lst)

    def compare_lists(self):
        mean1 = self.calculate_mean(self.list1)
        mean2 = self.calculate_mean(self.list2)
        if mean1 > mean2:
            return "Первый список имеет большее среднее значение"
        elif mean2 > mean1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
comparator = ListComparator(list1, list2)
print(comparator.compare_lists())