import random

arr = [random.randint(1, 100) for _ in range(random.randint(7, 10))]


print(f"Исходные баллы: {arr}")

min_arr = min(arr)
max_arr = max(arr)

print(f"Удаляем минимум ({min_arr}) и максимум ({max_arr}).")

filter_add = arr.copy()
filter_add.remove(min_arr)
filter_add.remove(max_arr)

print(f"Оставшиеся баллы: {filter_add}")

average = sum(filter_add) / len(filter_add)
print(f"Средний рейтинг: {average}")