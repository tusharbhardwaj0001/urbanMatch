### Project Setup Instruction 
To Setup this project at your local, You need to perform below steps 
1. Python should be installed at your system
2. First You need to setup virtal environment, for that you need to run this command 
   - python3 -m venv urbanVenv  
3. Than you need to activate your virtual env.
   - If you are using Ubuntu System, Than you need to run 
      - source urbanVenv/bin/activate
4. Now, to install all the dependencies, you need to run 
   - pip install -r requirement.txt 
5. Now you just need to run 
   - To run in production mode 
      - fastapi run app/main.py
   - To run in dev mode 
      - fastapi dev app/main.py


**Prefer to use local database, like postgress , my sql
- reason because, SQLlite doesn't support array data structure to store



### My Contribution 
I had work on 2 verticals for this assignment 
1. Create a folder structure, such that we can extend this directory structure in big scale 
    1. Folder structure matters when project get large and multiple persons work.
    2. To give Structure to this project, I have done some changes 
        1. I have move all the codes under the app directory , and parllael to app, other than business logic folders exist like virtual env, requirement.txt and other all files ,which doesn't impact our buisness logic.
        2. Inside the app directory, at first step I have main file, schema file, models and database file 
        3. to create all routes, I have create a folder routers, inside this users.py file contain all the routes.
        4. To handle all exceptions, I have create a exceptions folder, hanlders.py file will export all the error class

2. Working on necessary logics and validation.


### Tasks Explnation:
1. Add User Update Endpoint:
   - I have create a PATCH route, through which we can do partial update as well
   - Reason behind creating PATCH method, to restrict minimal data flow over the network.
2. Add User Deletion Endpoint:
   - I have create a DELETE route, through which we can delete entry for that user.
   - I have pick user_id from query params.
   - We don't have active_status currently, otherwise better way to made inactive function over DELETE
3. Find Matches for a User:
   - I have create a GET route, through which we can get list of users who might be perfect match for current user.
   - I define perfect match on the basis of certain metrics like.
        - Perfect match shold be opposite gender
        - Age gap should be +- 5.
        - Both having same type of interests.
   - You will get all the match in order of same interests.
4. Add Email Validation:
   - I have add this validation on Schema level. 


  

- I have addedd Postman collection export, You can import that collection in postman and test all the routes.
