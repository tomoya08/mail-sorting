#メールからPDF化したファイルをテキストファイル化
from totxt import convert_pdf_to_txt
#テキストファイル化したものから商品を抽出
from aggregated import aggregated
import glob

if __name__ == '__main__':
        file_list = glob.glob('/Users/mizumuratomoya/Desktop/pythontomo2/*.pdf')
        result_list = []
        for item in file_list:
            result_txt = convert_pdf_to_txt(item)
            result_list.append(result_txt)

        allText = ','.join(result_list) # PDFごとのテキストが配列に格納されているので連結する

        with open('pdf.txt', 'w') as file:
                file.write(allText)
        aggregated()
