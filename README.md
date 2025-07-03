# 🔢 ankLekhan

ankLekhan is a standalone desktop application built with Python and Streamlit. It can be run with or without a Python interpreter installed on the system. This repository includes everything you need to either run the app directly or build your own executable using PyInstaller.

### 🚀 Features
1. Run Python-based Streamlit app as a standalone .exe file
2. No need for Python interpreter on target machines
3. Automatic launch in the browser on http://localhost:8501/
4. Easy-to-follow build process using PyInstaller.

## 📁 Project Structure

      | Folder/File        | Purpose                                                          |
      | ------------------ | ---------------------------------------------------------------- |
      | `application/`     | All Python modules and logic are stored here                     |
      | `hooks/`           | PyInstaller hook scripts (e.g., to include Streamlit properly)   |
      | `config/`          | Static resources                                                 |
      | `ankLekhan.py`     | Main script to launch the Streamlit app                          |
      | `ankLekhan.spec`   | PyInstaller configuration file                                   |
      | `requirements.txt` | Lists all Python packages required to run the app                |
      | `ankLekhan.exe`    | Auto-generated final .exe (after build)                          |


## 🛠️ Running the Application
  There are two options:
  #### ✅ Option 1: Run the Executable (No Python Required)
  If you don’t have Python installed, simply run **"ankLekhan.exe"** file.    
  Once started, it will open in your default browser at: http://localhost:8501/
    
  #### ✅ Option 2: Run Using Python
  If you have Python installed:
  ##### 🧰 Install Dependencies
    pip install -r requirements.txt
    
  
  ##### Run the app:
    python ankLekhan.py

  This will also launch the app at http://localhost:8501/.

## 🏗️ Build Instructions
  Steps to create a standalone .exe file using PyInstaller:
  
  1. Write application logic inside the application/ folder.
  2. Create a hooks/ folder and add a custom hook for streamlit.
  3. Generate the .spec file:
      ```bash
     pyi-makespec --onefile --additional-hooks-dir=./hooks ankLekhan.py
       ```
    
  5. Update the generated ankLekhan.spec file: add paths for datas, hookspath, and hiddenimports as needed.
  6. Build the executable:
     ```bash
         pyinstaller ankLekhan.spec --clean
      ```
 


