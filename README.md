# Project Setup

After cloning the repository, follow these steps to set up the project:

1. Create a virtual environment:
   ```bash
   python -m venv venv

2. Activate the virtual environment:
   on Windows:
   venv\Scripts\activate
   
   on macOS/Linux:
   source venv/bin/activate

3.Install the required packages:
  pip install -r requirements.txt


#Custom Management Command
This project includes a custom management command:

  python manage.py populate_db

Warning
Executing this command will create a large number of instances in your database:

5,000,000 User instances
4,000,000 Contract instances
3,200,000 RecurrentContract instances
Please be aware of the potential impact on your system's resources and perform this action at your own risk.
