import os
import shutil

def convert_to_zip(folder_names):
    for lambda_folder_name in folder_names:
        os.chdir(lambda_folder_name)
        shutil.make_archive("lambda_code", 'zip')
        shutil.move("lambda_code.zip","..\\..\\CloudFormation\\")

if __name__ == "__main__":
    lambda_folder_names = ["Code\\lambda_code"]
    convert_to_zip(lambda_folder_names)
    