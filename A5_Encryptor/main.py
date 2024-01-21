import json

result_text = ''
chr = ''

user_select = int(input('1.encode 2.decode 3.exit : '))
if user_select == 1:
    user_input = str(input('TEXT : '))

    with open('./data/translate_datas.json', 'r') as f:
        translation_data = json.load(f)

    for texts in user_input:
        if texts in translation_data:
            result_text += str(translation_data[texts])
        else:
            result_text += str(texts)

    print(f'encoded_text : {result_text}')

elif user_select == 2:
    user_input = input('ENCODED STRING : ')

    with open('./data/decode_data.json', 'r') as f:
        decode_translation_data = json.load(f)

    for texts in user_input:
        if texts.isdigit():
            chr += texts
            if len(chr) == 2:
                result_text += str(decode_translation_data[chr])
                chr = ''
        elif not str(texts) in decode_translation_data:
            result_text += texts

    print(f'decoded text : {result_text}')
