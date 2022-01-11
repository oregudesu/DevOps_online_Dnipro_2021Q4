# Module 3 Database Administration

## Task 4.1

### Part 1

1. I downloaded and installed the last version of MySQL Server to my VM (steps 1-2):

![downloading and installing MySQL Server](./images/1.png?raw=true)

Then I ran `sudo mysql_secure_installation` for configure mysql.

2. I wanna create a Company database with tables: employees, teams, projects. Each employee has the information about first and last name, age and company position. Employees can team up and one employee can be the member of several teams. Team can participate in the project development. Several teams can work on one project and one team can work at several projects (step 3). So first of all I've created the 'company' database (step 4): 

![creating the 'company' database](./images/2.png?raw=true)

Then I created three tables: employees, teams and projects:

![creating 'employees', 'teams' and 'projects' tables](./images/3.png?raw=true)

To connect tables with many-to-many connection I created two additional tables: team_employees and project_teams:

![creating 'team_employees' and 'project_teams' tables](./images/4.png?raw=true)

And I totally forgot to specify an 'age' column in 'employees' table, so I did it with `alter table` query:

![specifying an 'age' column in 'employees' table](./images/5.png?raw=true)

So in overall there are five tables in the 'company' database:

![tables in the 'company' database](./images/6.png?raw=true)
![definition of tables from 'company' database](./images/7.png?raw=true)

Now lets fill them in (step 5):

![the 'employees' table](./images/8.png?raw=true)
![the 'teams' table](./images/9.png?raw=true)
![the 'team_employees' table](./images/10.png?raw=true)
![the 'projects' table](./images/11.png?raw=true)
![the 'project_teams' table](./images/12.png?raw=true)

3. Let's get positions count of employees that less than 30 years old from team #1 and show it in descending order (step 6):

![getting positions count of employees that less than 30 years old from team #1 in descending order](./images/13.png?raw=true)

4. According to step 7 I needed to make next SQL queries:

 - DDL: **Data Definition Language**: 
 
  I created a table in the 'company' database:
  
![creating the 'test' table](./images/14.png?raw=true)

  Then I added to it one more column - 'experience':
  
![adding the row 'experience' to the 'test' table](./images/15.png?raw=true)

  I renamed that table to 'worker':
  
![renaming the table 'test' to 'worker'](./images/16.png?raw=true)

  and renamed the 'name' column to 'first_name':
  
![renaming the column 'name' to 'first_name'](./images/17.png?raw=true)

  (Here I noticed that MariaDB has a lil bit different syntax. For example, to rename a table column they use `change column old_name to new_name` instead of `rename column old_name to new_name` command)

  I filled in the table with some data:
  
![filling in the 'worker' table](./images/18.png?raw=true)

  Then I removed all data in the table:

![removing data from the 'worker' table](./images/19.png?raw=true)

  And removed the 'worker' table:
 
![dropping the 'worker' table](./images/20.png?raw=true)

 - DML: **Data Manipulation Language**:
 
  I created a new 'test' table and filled it in:
 
![creating the 'test' table](./images/21.png?raw=true)

  I updated 'column1' and 'column2' values on condition if 'column3' is less than 3:
  
![updating the 'test' table](./images/22.png?raw=true)

  I deleted rows in which the 'column3' is greater than 2:
  
![deleting rows in which the 'column3' is greater than 2 from the 'test' table](./images/23.png?raw=true)

 - DCL: **Data Control Language**:
  
  First of all I created one guest user:
  
![creating a guest user](./images/24.png?raw=true)

  Then I revoked all privileges from the user:
  
![revoking all privileges from the guest user](./images/25.png?raw=true)

  And granted to him/her only select privilege for the 'test' table in the 'company' database:
  
![granting a select privilege on the 'test' table for the guest user](./images/26.png?raw=true)

  I logged in as guest user:
  
![logging in as guest user](./images/27.png?raw=true)

  And tried to select and insert data from the 'test' table:
  
![trying to select and insert data into 'test' table](./images/28.png?raw=true)

  As shown above I could not do that because of restrictions. User 'guest' can only select data.
  
5. I created two more users for testing another privileges (step 8):

![creating two new users](./images/29.png?raw=true)

So in total I have three new users. For the first one I granted only select privilege to the 'company.test' table in the previous step. For the second I granted select and insert privileges and for the third - only delete privilege:

![granting privileges for new users](./images/30.png?raw=true)

Then I tested it out for the guest1 user:

![testing selection, insertion and deleting info for the guest1](./images/31.png?raw=true)

And for the guest2 user:

![testing selection, insertion and deleting info for the guest2](./images/32.png?raw=true)

As show above users can only do all their grants. 

6. I made a selection from 'mysql.db' table (step 9):

![selecting 'user' column from 'mysql.db' table](./images/33.png?raw=true)


### Part 2

1. I backed up my 'company' database (step 10):

![backing up the 'company' database](./images/34.png?raw=true)

2. I dropped the 'test' table from the 'company' database (step 11):

![dropping the 'test' table from the 'company' database](./images/35.png?raw=true)

3. Then I restored the database from backup1.sql (step 12):

![restoring the database](./images/36.png?raw=true)

And checked if the 'test' table is restored:

![checking on the 'test' table](./images/37.png?raw=true)

Yes, it is tho.

4. For transfer my database to the AWS RDS firstly I created a database instance there (step 13):

![creating a database instance on AWS RDS](./images/38.png?raw=true)

Then I got host info: 

![getting a host info from the instance](./images/39.png?raw=true)

I edited source IP in the security group's inbound rule for public access from anywhere:

![editing source IP in the security group's inbound rule](./images/40.png?raw=true)

And tried to connect to the database:

![connecting to remote database](./images/41.png?raw=true)

Yeah, I'm in, the connection's stable. Then I tried to restore my 'company' database:

![trying to resore my database](./images/42.png?raw=true)

But an error appeared. That is because my dump file doesn't have the "create database" statement, so mysql doesn't know what database I'm trying to use. I dumped the 'company' database again with --databases option:

![dumping the 'company' database with --databases option](./images/43.png?raw=true)

And tried to restore db one more time:

![trying to resore my database](./images/44.png?raw=true)

Success!

5. I connected to the remote database and selected all employees with age from 25 to 31 (steps 14-15):

![selecting all employees with age from 25 to 31 from the remote database](./images/45.png?raw=true)

6. I removed the 'test' table and created a dump (step 16):

![dropping the 'test' tabke and dumping the remote 'company' database](./images/46.png?raw=true)


### Part 3

1. I created a DynamoDB table (step 17):

![creating a DynamoDB table](./images/47.png?raw=true)

And filled it in (step 18):

![filling in the DynamoDB table with some data](./images/48.png?raw=true)

2. I made the query request to the database for fetching the student with the name 'Matt' (step 19):

![doing a query request to the db](./images/47.png?raw=true)

And made the scan request for fetching all students with grade not less than 3:

![doing a scan request to the db](./images/47.png?raw=true)

