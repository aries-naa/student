Feature: Копание в youtube.

Scenario: Задание 1
  given 1.1 Заходим на сайт 'http://www.youtube.com'
  when  1.2 Ищем 'behave python'
  when  1.3 Выводим первые '5' ссылок
  when  1.4 Открываем '3' ссылку
  then  1.5 Сохраняем в файл 'результат.txt' описание видео
