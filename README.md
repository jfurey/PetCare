# PetCare
A pet health tracking application for pet owners to keep track of everything pet-related in one place.

# About
PetCare provides a user-friendly interface for pet owners to monitor and record various health-related information about their pets. Whether it's tracking veterinary visits, vaccinations, or dietary habits, PetCare aims to simplify pet health management.

# Features
* Manage and view pet profiles.
* Track medical history, including vaccinations and vet visits.
* Monitor dietary habits and exercise routines.
* Share information with veterinarians or pet sitters.
* Access resources for pet ownership.

# Technologies Used
This project utilizes the following technologies:
* Backend: Python (Flask)
* Frontend: TypeScript (Angular), JavaScript, HTML, CSS
* Database: MySQL, hosted on AWS

# Documentation
* Frontend README: https://github.com/UNO-CSCI4830/PetCare/blob/main/frontend/README.md
* Database: https://github.com/UNO-CSCI4830/PetCare/wiki/AWS-RDS-Database-Documentation

# Installation and Running
1. Clone the repository: ```git clone https://github.com/UNO-CSCI4830/PetCare.git```
2. Navigate to the project directory: ```cd PetCare```
3. Set up the backend environment: ```cd backend```
   - To install dependencies: ```pip install -r requirements.txt```
4. Set up the frontend environment: ```cd ../frontend```
   - To install dependencies: ```npm install```
5. Run the application:
   - Start backend server: ```cd ../backend``` and then ```python app.py```
   - In a new terminal, start frontend server: ```cd ../frontend``` and then ```npm start```
  
Open your browser and navigate to ```http://localhost:4200```

# Team Members
Allison Coates, Julianne Furey, Sarah Lemi, Farrukh Gafurov, Osmar Carboney, Alexander Jimenez, Rohith Chandra Sai Talluri

## My Contributions
This fork of the original PetCare project was created for portfolio purposes.

As a core backend and database contributor, I completed the following:
- Set up the shared AWS RDS MySQL database and revised SQL scripts to ensure schema compatibility
- Developed `users.py` and `pets.py` with full CRUD functionality, error handling, and secure password hashing
- Configured backend connectivity, implemented image serving, and tested endpoints via API and database validation
- Maintained detailed backend/database documentation in the GitHub Wiki

Note: The AWS-hosted database has been shut down, so backend functionality is no longer live. The code remains available for reference.


