import os

def delete_file(file_path):
    
    if os.path.exists(file_path):
        
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"Файл {file_path} сәтті жойылды.")
            except Exception as e:
                print(f"Файлды жою кезінде ошибка пайда болды: {e}")
        else:
            print(f"Доступ жабык: {file_path} доступ шектеулі болғандыктан удаление жасау мүмкін емес.")
    else:
        print(f"Бұндай файл {file_path} жоқ.")