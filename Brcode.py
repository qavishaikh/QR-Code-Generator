import barcode
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode(data, file_name):
    # Create a barcode object
    code = Code128(data, writer=ImageWriter())

    # Generate the barcode and save it as an image
    code.save(file_name)

if __name__ == "__main__":
    while True:
        # Prompt the user for data to encode in the barcode
        data = input("Enter the data to encode in the barcode (or 'exit' to quit): ")
        
        if data.lower() == 'exit':
            break
        
        # Prompt the user for the filename for the barcode image
        file_name = input("Enter the filename for the barcode image (e.g., 'barcode.png'): ")

        # Generate the barcode
        generate_barcode(data, file_name)

        print(f"Barcode generated and saved as '{file_name}'")
