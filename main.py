import pickle 
import os.path 
from DriveAPI import DriveAPI
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request 
  
  
SCOPES = ['https://www.googleapis.com/auth/drive'] 
  
def tratamento(file_list):
    for file in file_list:
        print(file)


if __name__ == "__main__": 
    obj = DriveAPI() 
    i = int(input("Enter your choice:\n 1- Download file\n 2- Upload File\n 3- Get Files\n 4- Get Folders\n 5- Exit.\nResposta:")) 
      
    if i == 1: 
        f_id = input("Enter file id: ") 
        f_name = input("Enter file name: ") 
        obj.FileDownload(f_id, f_name) 
          
    elif i == 2: 
        f_path = input("Caminho inteiro: ") 
        f_nome = input("Nome do arquivo: ")
        obj.FileUpload(f_path, f_nome) 
    elif i == 3:
        quantidade = int(input("Quantidade de arquivos: "))
        result_dict = obj.getFileList(quantidade)
        file_list = result_dict.get('files') 
  
        for file in file_list: 
            print(file['name'])
    elif i == 4:
        result_dict = obj.getFileList()
        file_list = result_dict.get('files') 
        lista_folders = tratamento(file_list)
        
    else: 
        exit()