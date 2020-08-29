documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]


directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}

def number2name():
  number = input('Введите номер документа: ')
  for dict in documents:
    result_name  = ''
    # print(dict)
    # print (type(dict))
    if number == dict['number']:
      result_name = dict['name']
  if result_name:
    print('Документ с таким номером принадлежит: ' + result_name)
  else:
    print('Нет такого документа в архиве')
#number2name()

def number2shelf():
  number = input('Введите номер документа: ')
  for dict in documents:
    document = ''
    shelf = ''
    if number == dict['number']:
      for directory_number, directory_content in directories.items():
        #print(directory_number, directory_content)
        if number in directory_content: # т.к.  directory_content это список, то мы проверяем входит ли наш номер в список вот так:
          document = number
          shelf = directory_number
  if shelf:
    print(f'Документ номер {document} найден на полке номер {shelf}')
  else:
    print(f'Документ номер {number} не найден')
#number2shelf()

def list_documents():
  for dict in documents:
    print(dict['type'] + ' ' + '"' + dict['number'] + '"' + ' ' + '"' + dict['name'] + '"')
#list_documents()

def add_document():
  doc_type = input('Введите тип документа: ')
  number = input('Введите номер документа: ')
  name = input('Введите имя собственника: ')
  shelf = input('Введите номер полки для хранения: ')
  documents.append({"type": "doc_type", "number": "number", "name": "name"})
  if shelf in directories:
    documents.append({"type": doc_type, "number": number, "name": name})
    directories[shelf].append(number)
  else:
    print('Такой полки нет! Сформирована заявка на закупку новой полки. В настоящий момент рекомендуем вам воспользоваться имеющимися полками')
# add_document()



def main():
  user_input = input('Введите команду (P-people, S-shelf, L-list, A-add): ')
  if user_input == 'p':
    print('Вы выбрали функцию number2name():')
    number2name()
  elif user_input == 's':
    print('Вы выбрали функцию number2shelf():')
    number2shelf()
  elif user_input == 'l':
    print('Вы выбрали функцию list_documents():')
    list_documents()
  elif user_input == 'a':
    print('Вы выбрали функцию add_document():')
    add_document()
main()

