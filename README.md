## Table of Contents 
- [Code structure](#code-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)

## Code Structure

The code is structured as follows (in the iwd/IWD/IWD/core folder):

- The endpoints are at **urls.py**
- The views are at **views.py**
- The models are at **models.py**
- The forms are at **forms.py**
- The tests are at **tests.py**

## Prerequisites

Install the following prerequisites:

1. [Python 3.10.4 or higher](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/download), or any code editor.


## Installation
### 1. Clone the repository in root directory:
```bash
git clone https://github.com/oussachi/Receipt-Tracker
```

### 2. Create a virtual environment

From the **root** directory run:

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 4. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

### 5. Run migrations

Make sure your current location looks something like **root\Receipt-Tracker** and run the following commands:

```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
### 6. Run the development server
```bash
python3 manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.