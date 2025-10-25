def add_to_shopping_list(item, shopping_list):
    """
    Добавляет товар в список покупочек
    """
    # Добавляем товар в список
    shopping_list.append(item)
    print(f"Ура, '{item}' у нас в пакете!")

def main():
    """
    Основная функция программы
    """
    # Создаем пустой список для покупок
    my_shopping_list = []

    print("=== СПИСОК ПОКУПОК ===")

    # Добавляем товары в список
    add_to_shopping_list("Хлеб", my_shopping_list)
    add_to_shopping_list("Молоко", my_shopping_list)
    add_to_shopping_list("Яблоки", my_shopping_list)

    # Показываем итоговый список
    print(f"\nВаш список покупок: {my_shopping_list}")
    print(f"Всего товаров: {len(my_shopping_list)}")

if __name__ == "__main__":
    main()