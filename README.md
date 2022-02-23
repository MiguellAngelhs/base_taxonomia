# base_taxonomia

# Install
- python3 -m venv env
- source env/bin/activate
- cd base_taxonomia
- pip3 install -r requirements.txt
- python manage.py makemigrations;
- python manage.py migrate; 
- python manage.py createsuperuser;
- python3 -m pip install --upgrade pip
- python3 -m pip install --upgrade Pillow
- sudo apt install mupdf
- sudo apt install libmupdf-dev
- pip3 install PyMuPDF==1.16

- uninstall pymupdf
- pip uninstall fitz
- pip install pymupdf
- pip install python-docx
- pip install mysql-connector-python

# Para text full search en MySQL
Desde la terminal se ejecuta el comando
- mysql -u [nombre del MySQL] -p;
- show databases;
- use pb_taxonomia;
- CREATE FULLTEXT INDEX indexfileinfo ON extraccion_taxonomia (file,directory,transcription);



# .env
- Crear archivo .env