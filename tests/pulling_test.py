import pulling.Avro as avro
import pulling.Json as json
import pulling.Csv as csv
import pulling.Pdf as pdf
import pulling.Docx as docx
import pulling.Rtf as rtf
import pulling.Txt as txt


def test_avro():
    schema = {
        'doc': 'A weather reading.',
        'name': 'Weather',
        'namespace': 'test',
        'type': 'record',
        'fields': [
            {'name': 'station', 'type': 'string'},
            {'name': 'time', 'type': 'long'},
            {'name': 'temp', 'type': 'int'},
        ],
    }
    records = [
        {'station': '011990-99999', 'temp': 0, 'time': 1433269388},
        {'station': '011990-99999', 'temp': 22, 'time': 1433270389},
        {'station': '011990-99999', 'temp': -11, 'time': 1433273379},
        {'station': '012650-99999', 'temp': 111, 'time': 1433275478}
    ]

    path = 'example.avro'

    avro.write_data(path, schema, records)

    found_data = avro.find_data(path, schema, ['-11'])
    print(f'found: {found_data}')

    new_schema = avro.replace_data(path, schema, path, {'011990-99999': '..numbers..', 'temp': 'key'})
    print(new_schema)

    result_data = avro.get_data(path, schema)
    print(f'result: {result_data}\n')


def test_json():
    data = {
        'list': [1, 2, 3, 4, 5],
        'president': {'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian', 'just_number': 2}
    }
    path = 'example.json'

    json.write_data(path, data)

    found_data = json.find_data(path, ['list', 'Zaphod Beeblebrox'])
    print(f'found: {found_data}')

    json.replace_data(path, path, {2: '2', 'list': 'List'})

    result_data = json.get_data(path)
    print(f'result: {result_data}\n')


def test_csv():
    data = [['Name', 'Age'], ['ItYaS', '16'], ['Dore', '13']]
    path = 'example.csv'

    csv.write_data(path, data)

    found_data = csv.find_data(path, ['ItYaS'])
    print(f'found: {found_data}')

    csv.replace_data(path, path, {'16': '17'})

    result_data = csv.get_data(path)
    print(f'result: {result_data}\n')


def test_pdf():
    path = 'example.pdf'

    result_text = pdf.get_text(path)
    print(f'result: {result_text}')

    found_text = pdf.find_text(path, ['World'])
    print(f'found: {found_text}\n')


def test_docx():
    path = 'example.docx'

    result_text = docx.get_text(path)
    print(f'result: {result_text}')

    found_text = docx.find_text(path, ['World'])
    print(f'found: {found_text}\n')


def test_rtf():
    text = ['Hello World. ', 'It is ItYaS!']
    path = 'example.rtf'

    rtf.write_text(path, text)

    result_text = rtf.get_text(path)
    print(result_text)

    found_text = rtf.find_text(path, ['World'])
    print(f'found: {found_text}')

    rtf.replace_text(path, path, {'ItYaS!': 'ItYaS.'})

    result_text = rtf.get_text(path)
    print(f'result: {result_text}\n')


def test_txt():
    text = ['Hello World.', 'It is ItYaS!']
    path = 'example.txt'

    txt.write_text(path, text)

    result_text = txt.get_text(path)
    print(result_text)

    found_text = txt.find_text(path, ['World'])
    print(f'found: {found_text}')

    txt.replace_text(path, path, {'ItYaS!': 'ItYaS.'})

    result_text = txt.get_text(path)
    print(f'result: {result_text}\n')


if __name__ == '__main__':
    print('____________________AVRO____________________\n')
    test_avro()

    print('____________________JSON____________________\n')
    test_json()

    print('____________________CSV____________________\n')
    test_csv()

    print('____________________PDF____________________\n')
    test_pdf()

    print('____________________DOCX____________________\n')
    test_docx()

    print('____________________RTF____________________\n')
    test_rtf()

    print('____________________TXT____________________\n')
    test_txt()
