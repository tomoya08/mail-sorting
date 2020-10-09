import re

def extract_text_in_file(filepath, pattern_prev, pattern_next):
    extracted_text_array = []
    pattern = pattern_prev + '(.*)' + pattern_next
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            tmp_extracted_text_array = re.findall(pattern, line)
            extracted_text_array.extend(tmp_extracted_text_array)

    return extracted_text_array

filepath = '/Users/mizumuratomoya/Desktop/pythontomo2/pdf.txt'
pattern_prev = '商品名 : '
pattern_next = '　ティーパック'
extracted_text_array = extract_text_in_file(filepath, pattern_prev, pattern_next)

for extracted_text in extracted_text_array:
    print(extracted_text)

# 出力
# 2020/02/01
# 2020/02/02
