import subprocess
import sys

# Install required packages if they're missing
required_packages = ['requests', 'Pillow', 'PyPDF2']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

import requests
from PIL import Image
from PyPDF2 import PdfMerger
import io
import os
from urllib.parse import urlparse, parse_qs, urlencode
from dataclasses import dataclass
from typing import List
import tempfile

BATCH_SIZE = 10  # Number of pages to process at once

@dataclass
class DocumentInfo:
    token: str
    start_page: int
    end_page: int
    output_filename: str

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_filename(prompt):
    while True:
        filename = input(prompt).strip()
        filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_'))
        
        if not filename:
            print("Please enter a valid filename.")
            continue
        
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'
        
        return filename

# [Rest of the code remains the same as in the previous version]
def get_document_info(doc_num: int) -> DocumentInfo:
    print(f"\n--- Document #{doc_num} Details ---")
    token = input(f"Enter token for document #{doc_num}: ").strip()
    
    while True:
        start_page = get_valid_integer_input(f"Enter start page for document #{doc_num}: ")
        end_page = get_valid_integer_input(f"Enter end page for document #{doc_num}: ")
        
        if end_page >= start_page:
            break
        print("End page must be greater than or equal to start page.")
    
    filename = get_valid_filename(f"Enter name for PDF file #{doc_num} (will add .pdf if needed): ")
    
    return DocumentInfo(
        token=token,
        start_page=start_page,
        end_page=end_page,
        output_filename=filename
    )

def download_page(base_url, page_number, token):
    parsed_url = urlparse(base_url)
    query_params = parse_qs(parsed_url.query)
    
    query_params.update({
        'page': [str(page_number)],
        'token': [token],
        'zoom': ['100'],
        'format': ['png']
    })
    
    new_query = urlencode(query_params, doseq=True)
    new_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{new_query}"
    
    try:
        response = requests.get(new_url)
        response.raise_for_status()
        return Image.open(io.BytesIO(response.content))
    except Exception as e:
        print(f"Error downloading page {page_number}: {e}")
        return None

def save_images_as_pdf(images, output_filename):
    if not images:
        return False
    
    rgb_images = [img.convert('RGB') for img in images]
    
    try:
        rgb_images[0].save(
            output_filename,
            save_all=True,
            append_images=rgb_images[1:],
            format='PDF'
        )
        return True
    except Exception as e:
        print(f"Error saving PDF: {e}")
        return False

def process_batch(base_url, token, start_page, end_page, output_filename):
    downloaded_images = []
    
    for page in range(start_page, end_page + 1):
        print(f"Downloading page {page}...")
        img = download_page(base_url, page, token)
        if img:
            downloaded_images.append(img)
        else:
            print(f"Failed to download page {page}")
    
    if downloaded_images:
        return save_images_as_pdf(downloaded_images, output_filename)
    return False

def scrape_and_save_pdf(base_url: str, doc_info: DocumentInfo) -> bool:
    print(f"\nProcessing: {doc_info.output_filename}")
    print(f"Pages {doc_info.start_page} to {doc_info.end_page}")
    
    # Create a temporary directory for batch PDFs
    with tempfile.TemporaryDirectory() as temp_dir:
        batch_pdfs = []
        merger = PdfMerger()
        
        # Process pages in batches
        current_page = doc_info.start_page
        while current_page <= doc_info.end_page:
            batch_end = min(current_page + BATCH_SIZE - 1, doc_info.end_page)
            batch_filename = os.path.join(temp_dir, f"batch_{current_page}_{batch_end}.pdf")
            
            print(f"Processing batch: pages {current_page} to {batch_end}")
            if process_batch(base_url, doc_info.token, current_page, batch_end, batch_filename):
                batch_pdfs.append(batch_filename)
            
            current_page = batch_end + 1
        
        # Merge all batch PDFs
        if batch_pdfs:
            print("Merging batches...")
            for pdf in batch_pdfs:
                merger.append(pdf)
            
            merger.write(doc_info.output_filename)
            merger.close()
            
            print(f"Successfully created {doc_info.output_filename}")
            return True
    
    print(f"Failed to create PDF for document")
    return False

def main():
    base_url = "https://media.ctump.edu.vn/DocImage.axd"
    
    print("=== Document Scraper ===")
    print("--- Input Phase ---")
    num_documents = get_valid_integer_input("Enter how many documents to download: ")
    
    documents: List[DocumentInfo] = []
    for doc_num in range(1, num_documents + 1):
        doc_info = get_document_info(doc_num)
        documents.append(doc_info)
    
    print("\n=== Summary of Documents to Process ===")
    for i, doc in enumerate(documents, 1):
        print(f"Document #{i}:")
        print(f"  - Pages: {doc.start_page} to {doc.end_page}")
        print(f"  - Output: {doc.output_filename}")
    input("\nPress Enter to start processing...")
    
    print("\n--- Processing Phase ---")
    for i, doc_info in enumerate(documents, 1):
        scrape_and_save_pdf(base_url, doc_info)
        print(f"Completed document {i} of {num_documents}")
        print("-" * 40)

if __name__ == "__main__":
    main()