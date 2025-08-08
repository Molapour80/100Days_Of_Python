import glob
import os
from datetime import datetime

def merge_text_files(input_pattern=r"E:\100Days_python\DAY_57\*.txt", 
                    output_file=r"E:\100Days_python\DAY_57\merged_output.txt",
                    add_separators=True,
                    include_filenames=True,
                    encoding="utf-8",
                    add_timestamp=True):
    """
    Merges multiple text files into one
    
    Parameters:
        input_pattern (str): Pattern to match files (e.g., *.txt)
        output_file (str): Output filename
        add_separators (bool): Add separators between files?
        include_filenames (bool): Include source filenames in output?
        encoding (str): File encoding to use
        add_timestamp (bool): Add creation timestamp to output?

    """
    
    # Get list of files matching the pattern:))))
    file_list = glob.glob(input_pattern)
    
    if not file_list:
        print("No files found matching the pattern!")
        return
    
    print(f"Merging {len(file_list)} files...")
    
    try:
        with open(output_file, 'w', encoding=encoding) as outfile:
            # Add header to output file____>>>>>_____
            if add_timestamp:
                outfile.write(f"Merged File - Created at {datetime.now()}\n\n")
            
            for filename in file_list:
                if include_filenames:
                    outfile.write(f"\n{'._.' * 40}\n")
                    outfile.write(f"File: {os.path.basename(filename)}\n")
                    outfile.write(f"{'.-.' * 40}\n\n")
                
                try:
                    with open(filename, 'r', encoding=encoding) as infile:
                        content = infile.read()
                        outfile.write(content)
                        
                        # Ensure proper spacing between files#_#
                        if add_separators and not content.endswith('\n'):
                            outfile.write("\n")
                            
                except UnicodeDecodeError:
                    print(f"Error reading 00{filename} - encoding issue suspected")
                except Exception as e:
                    print(f"Error processing 0-0{filename}: {str(e)}")
                
                if add_separators:
                    outfile.write("\n\n" + "-f-" * 50 + "\n\n")
            
        print(f"Successfully.-. created merged file: {output_file}")
        print(f"Output file size: {os.path.getsize(output_file)} bytes")
        
    except Exception as e:
        print(f"Error writing output file: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Merge all txt files in current directory with default settings
    merge_text_files()
    
    # Custom merge example:
    # merge_text_files(input_pattern="notes_*.md", 
    #                 output_file="all_notes.md",
    #                 add_separators=False,
    #                 encoding="utf-8-sig")