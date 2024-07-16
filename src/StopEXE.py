import psutil
import tkinter as tk
from tkinter.simpledialog import askstring


def close_app() -> None:
    root = tk.Tk()
    root.tk.eval(f'tk::PlaceWindow {root._w} center')
    root.withdraw()
    app_exe_file_name=askstring("CloseApp","Enter App EXE File Name:",parent=root)

    processArr = (process for process in psutil.process_iter() if process.name()==app_exe_file_name)
    try:
        next_process = next(processArr) #  this line will reduce the size by one
    except StopIteration:
        print(f"No running Process [ {app_exe_file_name} ] Closed")
    # Recreate the iterator so that the for loop goes over the entire list
    processArr = (process for process in psutil.process_iter() if process.name()==app_exe_file_name)
    
    try:
        for process in processArr:
            process.kill()
            print(f'[ {app_exe_file_name} ] is now closed')
    except Exception as e:
        print(f'[ {app_exe_file_name} ] could not be closed')
        print(f'[ {e} ] ')

if __name__ == "__main__":
    close_app()
