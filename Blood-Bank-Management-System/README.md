
# Blood Bank Management System

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## About the Project
The **Blood Bank Management System** is a web-based application designed to facilitate blood donation, requests, and management of donor records efficiently. This project aims to bridge the gap between blood donors and recipients by maintaining an up-to-date database of blood availability and donor details.

## Features
- **Landing Page** with an appealing UI
- **Donor Registration** with full details
- **Blood Request Form** for patients in need
- **Blood Availability Checker** to view available blood groups
- **List of All Donors** with search functionality
- **Contact Page** for inquiries
- **Responsive Design** for desktop and mobile users

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database:** MySQL


## Project Structure
```
BloodBankManagementSystem/
│-- static/
│   │-- css/style.css
│   │-- js/query.js
│   │-- images/
│-- templates/
│   │-- index.html
│   │-- blood_availability.html
│   │-- request_blood.html
│   │-- donors_registration.html
│   │-- donors_list.html
│   │-- contact.html
│-- app.py
│-- config.py
│-- requirements.txt
│-- README.md
│-- Blood_Bank.sql
│-- test_db.py
```

## Installation
### Prerequisites
- Python 3.12
- MySQL
- Flask Framework

### Steps
1. **Clone the Repository**
   ```cmd
   git clone https://github.com/your-username/blood-bank-management.git
   cd blood-bank-management
   ```
2. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```
3. **Set Up MySQL Database**
   - Create a MySQL database named `blood_bank`
   - Execute the `database.sql` file to create tables
4. **Run the Flask Application**
   ```bash
   python app.py
   ```
5. **Access the Application**
   Open your browser and visit: `http://127.0.0.1:5000`

## Usage
- Register as a donor with personal details
- Check available blood groups
- Request blood by filling out the form
- View a list of all registered donors

## Database Schema
- **Donors Table:** Stores donor details like name, blood group, contact info, etc.
- **Blood Requests Table:** Stores details of users requesting blood.

## Future Enhancements
- Implement user authentication (login/signup for donors and hospitals)
- Add an admin panel for managing requests and donors
- Integrate email notifications for blood requests and donor registrations
- Implement location-based donor search

## Contributing
Contributions are welcome! If you find a bug or want to add a feature, feel free to create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE] file for details.

