### Лабораторная работа по Git №4

## 1. Цели и задачи тестирования:
Определить основные цели тестирования, которые включают обнаружение
ошибок в программном коде, проверку его соответствия требованиям, а также
измерение его качества.
## 2. Описание тестируемого продукта:
Продукт, подлежащий тестированию, представляет собой программное
решение для быстрого нахождения площади и периметра фигур на плоскости.
Функциональность продукта включает в себя нахождение площади и периметра
геометрических фигур на плоскости.
Требования к продукту включают в себя корректное поведение функций при
входящих параметрах, не соответствующих нормам, правильность вывода
значений.
## 3. Область тестирования:
Тестирование всех методов возвращающих значение у файлов
## 4. Стратегия тестирования:
Использование ручного тестирования в качестве нахождения ключевых точек, и
добавление специальных unit тестов для таких случаев в корневую папку
репозитория. Ключевые точки - использование отрицательных чисел или нуля в
качестве длин сторон, радиусов в арифметических операциях.
## 5. Критерии приёмки:
Все ключевые точки обработаны unit тестами, и найдены ошибки при
выполнении, методы программы исправлены так, чтобы они работали
корректно.
 ## 6. Ожидаемые результаты:
Создание отчёта о дефектах, включающего описания найденных ошибок, шаги
и приоритеты исправления.
Предоставление статусов тестирования, включающих информацию о
количестве выполненных тестов и проценте успешно пройденных тестов.


| Название | Шаги | Ожидаемый результат |Pass/Fail |
|----------|----------|----------|----------|
| Отрицательные или нулевые вводимые данные (Негативный)   | Ввести при вызове функций отрицательные или равные нулю числа   | Неправильный вывод   | Fail     |
| Положительные вводимые данные (Позитивный)   | Ввести при вызове функций положительные числа   | Правильный вывод   | Pass   |
| Невозможные пропорции треугольника    | Ввести 3 стороны треугольника, при которых тот не может существовать   | Неккоректная работа программы   | Fail  |