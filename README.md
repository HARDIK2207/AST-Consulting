
# Indeed Job Scrapper

This Python-based web scraping project utilizes Selenium and BeautifulSoup to extract job listings for Python Developer positions in Gurgaon, Haryana, from Indeed.

## Table of Contents

- [Technologies Used](#features)
- [Features](#features)
- [Database Structure](#features)
- [Getting Started](#getting-started)
- [Overview](#Overview)
- [Contributing](#contributing)
  
## Technologies Used
Make sure you have the following installed before running the application:

- [Beatiful soup](https://pypi.org/project/beautifulsoup4/)
- [Selenium](https://www.selenium.dev/documentation/com/downloads/) 
- [Django](https://docs.djangoproject.com/en/5.0/)
- [Numpy](https://numpy.org/doc/)
- [MongoDB](https://www.mongodb.com/docs/)
## Features

- **Extracting** Utilizes Selenium and BeautifulSoup to extract job listings for Python Developer positions in Gurgaon, Haryana
- **Cleaning** The scraped data is then cleaned, including converting job salaries to per annum values and handling missing values.
- **Storage** The cleaned data is stored in a MongoDB database using MongoDB Compass and Atlas.
- **Admin Panel** An admin panel is implemented using Django to perform CRUD operations on the job data.


## Database Structure

The application uses a database table with the following structure:

| Field          | Type         | Description                  |
|----------------|--------------|------------------------------|
| job_title      | VARCHAR(255) | Title of the job position    |
| company_name   | VARCHAR(255) | Name of the hiring company   |
| company_location| VARCHAR(255) | Location of the company      |
| total_salary   | INT          | Annual salary for the job    |
| City           | VARCHAR(255) | City where the job is located|
| State          | VARCHAR(255) | State where the job is located|
| link           | VARCHAR(255) | Link to the job listing      |




## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/hardik2207/healthify.git
    cd ASTCONSULTING
    ```

2. **Run the Scrapper**
    ```bash
     run Job scrapper.py
    ```

5. **Run Admin Panel**
    ```bash
    python manage.py runserver
    ```

## Overview

- **Scrapped Jobs**
  
    ![Screenshot (392)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/9cf03c93-b047-41c4-a695-f1f6b43e95ec)

- **Cleaned Jobs**
   
    ![Screenshot (393)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/c4131a74-eece-4a46-82b4-60d08a6b3dc8)


- **Data stored in Mongodb**
  
    ![Screenshot (394)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/97340205-9111-4da5-9164-f4bc8738c3b8)
    ![Screenshot (395)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/fd864fdb-0e52-4167-bf4c-251dbab5e605)


- **Admin Panel using Django**
    1. **Admin Login**
    ![Screenshot (381)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/7d0075f4-3d90-4b4f-9aef-aadc7cfc668f)

    2. **Add Job**
        ![Screenshot (382)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/e25f4a76-8cec-4ed7-b1cb-0aaf58683ffa)
    3. **Search Job**
      ![Screenshot (396)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/6aed4a45-1f28-4976-94c6-db9735fcdd55)
    4. **Edit Job**
      ![Screenshot (391)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/500c5607-deb5-4875-ad06-9ee5c624f4ef)

    5. **Delete Job**
      
- **Mean salary of Python developers in Delhi**
    ![Screenshot (397)](https://github.com/HARDIK2207/AST-Consulting/assets/84044856/6c7ede8a-1670-46bf-bef5-1e48dd4f5c42)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.
