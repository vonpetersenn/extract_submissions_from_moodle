import os
import shutil
import argparse

#input: .zip that contains a folder of subfolders.
#One subfolder of format 'Firstname Name_number_assignesubmission_file' per student.
#Each subfolders is assumed to contain a single .pdf or .PDF file.

def main():
    parser = argparse.ArgumentParser(description='Copy PDF files from subfolders with a specified specifier.')

    parser.add_argument('--append', type=str, default='', help='Add a string to the end of the pdf name.')

    args = parser.parse_args()
    filename_appendix = args.append

    # Get folder path to input and output
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_folder_path = 'input'
    folder_path = os.path.join(script_dir, relative_folder_path)
    output_path = os.path.join(script_dir, 'output')
    temp_path = os.path.join(script_dir, 'temp')

    # check if the input folder contains a zip file and pass

    zip_file = None
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        zip_files = [f for f in os.listdir(folder_path) if f.endswith('.zip') or f.endswith('.ZIP')]
        if zip_files:
            zip_file = zip_files[0]
    else:
        print("The input folder does not exist or does not contain the .zip file")
        raise FileNotFoundError

    # now check that the temp folder exists and is empty:
    if os.path.exists(temp_path) and os.path.isdir(temp_path):
        shutil.rmtree(temp_path)
        os.makedirs(temp_path)
    else:
        os.makedirs(temp_path)

    # now unzip the zip file to the temp folder
    if zip_file == None:
        print("No zip file found in the input folder")
        raise FileNotFoundError
    else:
        zip_path = os.path.join(folder_path, zip_file)
        shutil.unpack_archive(zip_path, temp_path)
        print('Successfully unzipped ' + zip_file)

    # check that the output folder exists
    if os.path.exists(output_path) and os.path.isdir(output_path):
        shutil.rmtree(output_path)
        os.makedirs(output_path)
    else:
        os.makedirs(output_path)



    # now copy the pdf files from the subfolders to the output folder
    print('Copying pdf files...')
    subfolders = [f for f in os.listdir(temp_path) if os.path.isdir(os.path.join(temp_path, f))]
    counter = 0
    for subfolder in subfolders:
        subfolder_path = os.path.join(temp_path, subfolder)
        pdf_files = [f for f in os.listdir(subfolder_path) if f.endswith('.pdf') or f.endswith('.PDF')]
        if pdf_files:
            pdf_file = pdf_files[0]
            pdf_source_path = os.path.join(subfolder_path, pdf_file)
            new_pdf_name = subfolder.split('_')[0] + filename_appendix + '.pdf'
            pdf_destination_path = os.path.join(output_path, new_pdf_name)
            counter += 1
            shutil.copyfile(pdf_source_path, pdf_destination_path)
    print('Copied ' + str(counter) + ' pdf files.')

    # delete the temp folder
    shutil.rmtree(temp_path)
    print('Done.')

if __name__ == '__main__':
    main()