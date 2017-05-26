# SimpleHttpFS
A simple http API for remote FS

## Docs:
[Task](https://docs.google.com/document/d/1-fYdHDh9u87tMa395H2RbBq2bXFTi63irFiN0izc9Ug/edit?usp=sharing)


# Quickstart
```
git clone https://github.com/mav96/SimpleHttpFS.git
cd SimpleHttpFS
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

# Testing http API

We can now access to remote FS using the httpie command line tool...

- **/get** Downloads a file:
```
http -a admin:password123 GET http://localhost:8000/get/readme.txt > readme.txt
```

_Method_ GET

_Returns_: The specified file's contents

_Errors_:  404	The file wasn't found at the specified name
<br/>
<br/>
<br/>

- **/put** Uploads a file using PUT semantics.
```
http -a admin:password123 PUT http://localhost:8000/put/readme.txt < readme.txt
```
_Method_ PUT, POST

_Returns_: The metadata for the uploaded file.

_Errors_:  409	The call failed because a conflict occurred.
<br/>
<br/>
<br/>

- **/update** Update file 
```
http -a admin:password123 PUT http://localhost:8000/update/readme.txt < new_readme.txt
```

_Method_ PUT, POST

_Returns_: The metadata for the uploaded file.

_Errors_:  404	The file wasn't found at the specified name
<br/>
<br/>
<br/>

- **/meta** Retrieves file metadata.
```
http -a admin:password123 GET http://localhost:8000/meta/readme.txt
```
_Method_ GET

_Returns_: The metadata for the file

_Errors_:  404	The file wasn't found at the specified name
<br/>
<br/>
<br/>

- **/ls** List information about the FILEs
```
http -a admin:password123 GET http://localhost:8000/ls/
```
_Method_ GET

_Returns_: List of metadata entries for any matching files
<br/>
<br/>
<br/>

- **/rm** Deletes a file
```
http -a admin:password123 PUT  http://localhost:8000/rm/readme.txt
```
_Method_ PUT,POST

_Returns_: Metadata for the deleted file

_Errors_:  404	The file wasn't found at the specified name
<br/>
<br/>
<br/>

# Links
[Django REST framework](http://www.django-rest-framework.org/)

[A command line HTTP client](https://httpie.org/doc)
