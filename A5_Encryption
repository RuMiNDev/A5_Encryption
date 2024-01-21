import json


def encrypt(user_input):
    if not user_input:
        raise 'no rrt'
    result_text = ''
    with open('./data/encryption_data.json', 'r') as f:
        translation_data = json.load(f)

    for texts in user_input:
        if texts in translation_data:
            result_text += str(translation_data[texts])
        else:
            result_text += str(texts)

    return result_text

def decrypt(user_input):
    chr = ''
    result_text = ''

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

    return result_text

