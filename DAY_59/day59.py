import sys
import os

def search_in_file(file_path, search_terms):
    """
    Search for terms in a text file and display results with full file path
    
    Parameters:
        file_path (str): Path to the text file
        search_terms (list): List of terms to search for
    """
    try:
        # Get absolute file path
        full_path = os.path.abspath(file_path)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        results = {term: [] for term in search_terms}
        
        for line_num, line in enumerate(lines, 1):
            for term in search_terms:
                if term in line:
                    results[term].append((line_num, line.strip()))
        
        print(f"\nSearch results in file: {full_path}")
        print("✨" * 50)
        
        for term, matches in results.items():
            print(f"\nResults for '{term}':")
            print("-" * 40)
            if matches:
                for line_num, line in matches:
                    print(f"Line {line_num}: {line}")
            else:
                print("No matches found.")
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    # Hardcoded values for testing
    file_path = r"E:\100Days_python\DAY_59/example-fa.txt"  # Make sure this file exists in the same directory
    search_terms = ["Python"]     # Note: search_terms should be a list
    
    print(f"\nSearching for: {', '.join(search_terms)}")
    search_in_file(file_path, search_terms)