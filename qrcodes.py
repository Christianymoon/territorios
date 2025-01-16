import pandas as pd
import qrcode
import os

def read_excel_file(filepath):
    data = pd.read_excel(filepath)
    return data

def get_urls(dataset):
    urls = dataset['URL']
    return urls

def create_qr_code(url, name):
    qr = qrcode.make(url)
    qr.save(os.path.join('qr', name + '.png'))


if __name__ == "__main__":
    dataset = read_excel_file('Territorios URLS.xlsx')
    for data in zip(dataset['URL'], dataset['Nombre']):
        print(data, end="\n\n")
        create_qr_code(data[0], data[1])