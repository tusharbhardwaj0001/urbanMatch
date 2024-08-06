### Project Setup Instructions
To set up this project locally, please follow these steps:

Ensure Python is installed on your system.
1. Set up a virtual environment by running this command:
    -   python3 -m venv urbanVenv
2. Activate your virtual environment:
    -   If you are using an Ubuntu system, run:
        -    source urbanVenv/bin/activate
3. Install all the dependencies by running:
    -   pip install -r requirements.txt
4.  Run the application:
    1.  To run in production mode:
        -   fastapi run app/main.py
    2.  To run in development mode:
        -   fastapi dev app/main.py
** Note: It is preferred to use a local database such as PostgreSQL or MySQL. SQLite does not support array data structures for storage.

### My Contribution
I worked on two verticals for this assignment:

1. Create a folder structure:
    1.  Folder structure is crucial when the project scales and multiple people work on it.
        1.  To give structure to this project, I made the following changes:
        2.  Moved all code under the app directory. 
            1.  Parallel to app, other non-business logic folders exist, such as the virtual environment, requirements.txt, and other files.
            2.  Inside the app directory, I organized the main file, schema file, models, and database file.
            3.  Created a folder named routers to manage all routes. The users.py file inside this folder contains all the routes.
            4.  Created an exceptions folder to handle all exceptions, with handlers.py exporting all the error classes.
2.  Working on necessary logic and validations:

### Task Explanation
1. Add User Update Endpoint:
    - Created a PATCH route to allow partial updates.
    - The PATCH method is used to restrict minimal data flow over the network.
2.  Add User Deletion Endpoint:
    -   Created a DELETE route to delete user entries.
    -   Used user_id from query parameters.
    -   Ideally, we would have an active_status field to deactivate a user instead of deleting, but it is not currently available.
3.  Find Matches for a User:
    -   Created a GET route to retrieve a list of potential matches for a user.
    -   Defined a "perfect match" based on the following criteria:
        -   Opposite gender
        -   Age gap within ±5 years
        -   Shared interests
        -   Matches are returned in order of common interests.
4. Add Email Validation:
    -   Added email validation at the schema level.
    -   I have also included a Postman collection export. You can import this collection into Postman to test all the routes.

**Please review this file and let me know if there are any issues or further corrections needed.

Thanks and Regards,
Tushar Bhardwaj