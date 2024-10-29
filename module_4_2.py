def test_function():
    def inner_function():
        print('Я в области функции test_function')
    inner_function()

test_function() # Успешный вызов функции inner_function()
inner_function() # Ошибочный вызов функции inner_function()