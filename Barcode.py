import barcode
from barcode.writer import ImageWriter

def generate_barcode(number):
    barcode_format = barcode.get_barcode_class('upc')
    barcode = barcode_format(number, writer=ImageWriter())
    barcode.save('barcode')

if __name__ == '__main__':
    generate_barcode(123456789012)