def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)


# --- Тести ---
process_list([1, 2, 3])
process_list([5, 8])
process_list(["a", "b", "c", "d"])
