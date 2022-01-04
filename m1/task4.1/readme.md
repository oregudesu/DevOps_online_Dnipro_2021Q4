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

!['employees' table](./images/8.png?raw=true)
!['teams' table](./images/9.png?raw=true)
!['team_employees' table](./images/10.png?raw=true)
!['projects' table](./images/11.png?raw=true)
!['project_teams' table](./images/12.png?raw=true)

3. Let's get positions count of employees that less than 30 years old from team #1 and show it in descending order (step 6):

![getting positions count of employees that less than 30 years old from team #1 in descending order](./images/13.png?raw=true)





























