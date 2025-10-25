import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except Exception as e:
        logging.error("Error when dividing numbers", exc_info=True)
        print("An error occurred! Details are recorded in the log.")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 5)
