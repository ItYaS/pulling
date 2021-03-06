# Формат .csv
Вызов функций этого формата:

```python
import pulling.Csv as csv

csv.function(arguments)
result = csv.function(arguments)
```
## Возможные методы:
**get_data(** *path* **)** - функция, которая возвращает данные из файла, в виде списка, где каждый вложенный список - это строка из файла, а элементы вложенного списка - это столбцы в строке.

 - *path* - путь к нужному файлу.


**find_data(** *path*, *pattern_list* **)** - функция, которая возвращает совпадения из данных файла в виде словаря, где ключ - это шаблон поиска, а значение - это список с найденными совпадениями.

 - *path* - путь до нужного файла.

 - *pattern_list* - список с шаблонами, где каждый шаблон является отдельным элементом списка.


**write_data(** *path*, *data_list*, *mode='w'* **)** - функция, которая записывает данные в файл и сохраняет его.

 - *path* - путь файла в который надо записать данные.

 - *data_list* - список, где каждый вложенный список это строка, которую нужно сохранить в файле. А элементы вложенного списка - это столбцы в строке.

 - *mode* - режим открытия файла. По умолчанию стоит режим чтения 'w'.



**replace_data(** *path*, *new_path*, *replacement_dict* **)** - функция, которая принимает словарь с данными, заменяет данные и сохраняет эти изменения в новом файле.

 - *path* - путь файла из которого надо взять данные.

 - *new_path* - путь файла, в который надо записать изменения. Если ввести тот же путь, то изменения сохранятся в этом файле.

 - *replacement_dict* - словарь с данными, где ключи словаря - это данные, которые надо заменить, а значение элементов словаря - данные на которые надо заменить.