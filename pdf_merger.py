import logging
import os
from pypdf import PdfWriter, PdfReader

# Configure logging to ignore messages below ERROR level
logging.basicConfig(level=logging.ERROR)

def merge_entire_pdfs(pdf_list, result_name):
    writer = PdfWriter()

    for pdf in pdf_list:
        reader = PdfReader(pdf)
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

    with open(result_name + ".pdf", 'wb') as out:
        writer.write(out)

    print("PDFs merged successfully!")

def merge_specific_pages(pdf_list, result_name):
    writer = PdfWriter()

    for pdf in pdf_list:
        while True:  # Add a loop to ensure valid input
            page_range = input(f"Enter the range of pages to merge for {pdf} (e.g., '1,3' or '2' for a single page): ")
            try:
                # Split the input and convert to integers
                pages = tuple(map(int, page_range.split(',')))

                # Check if the page numbers are within the correct range
                if len(pages) == 1:
                    pages = (pages[0], pages[0])  # Single page specified, make it a range
                elif len(pages) != 2:
                    raise ValueError("Please enter two numbers for the range.")

                # Assume the first number should be less or equal to the second number
                if pages[0] > pages[1]:
                    raise ValueError("The start page must be less than or equal to the end page.")

                # Use reader to check if the specified pages are within the PDF page count
                reader = PdfReader(pdf)
                if pages[1] > len(reader.pages) or pages[0] < 1:
                    raise ValueError("One or more page numbers are out of the PDF's page range.")

                # If all checks pass, break the loop and proceed
                break

            except ValueError as e:
                print(f"Invalid input: {e}. Try again.")
            except IndexError:
                print("An error occurred processing the pages. Please ensure your input is correct.")

        # Add specified pages to the writer
        for page in range(pages[0]-1, pages[1]):
            writer.add_page(reader.pages[page])

    # Write out the resulting PDF
    with open(result_name + ".pdf", 'wb') as out:
        writer.write(out)

    print("Specific pages of PDFs merged successfully!")

def collect_pdf_files():
    pdf_list = []
    
    while True: 
        try:
            n = int(input("How many PDFs would you like to merge? :"))
            break  # Exit the loop if the input is a valid integer

        except ValueError:
            print("Please enter a valid number. \n")  # Inform the user of the error

    for i in range(n):
        while True:
            pdf_name = input(f"Enter the name of PDF file {i+1} with .pdf extension: ")
            if os.path.exists(pdf_name):
                pdf_list.append(pdf_name)
                break  # Exit the loop if file exists
            else:
                print(f"No such file: {pdf_name}")
                retry = input("Press 'R' to retry entering this file, or 'M' to return to the main menu: ").upper()
                if retry == 'M':
                    return None  # Return None to signal return to the menu
                # If 'R', the loop will continue and ask again

    return pdf_list


def main():
    while True:
        print("\n1. Merge entire PDFs")
        print("2. Merge specific pages of the PDFs")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1' or choice == '2':
            pdf_list = collect_pdf_files()
            if pdf_list is None:
                continue  # Go back to the main menu 
            
            result_name = input("Enter the name of the resultant PDF: ")

            if choice == '1':
                merge_entire_pdfs(pdf_list, result_name)

            elif choice == '2':
                merge_specific_pages(pdf_list, result_name)

        elif choice == '3':
            print("Exiting application!")
            break

        else:
            print("\nInvalid Choice! Please enter a number between 1-3.")

if __name__ == "__main__":
    main()