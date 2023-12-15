# Team Project repo

![Build Status](https://app.travis-ci.com/gcivil-nyu-org/INET-Monday-Fall2023-Team-4.svg?branch=develop) ![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/INET-Monday-Fall2023-Team-4/badge.svg?branch=develop)


Detailed team Monday Team 4 project proposal 

TL;DR 


….

Project Summary 


Project Name
Short Description
Team Enthusiasm Rank
*1-10
Team Confidence - YES we can do this in time!
*1-10
Product Owner.
*Who will own this for the team?
Check Out
Book club organization tool
9.4
8.4
Zoila Rodriguez Rivera



Projects Details:
Name: Check Out

What is the name of the project you want to develop? Check Out
Description

What is the project you want to develop? (Description in less than 250 words)

Check Out is an application with the potential to organize book clubs at your local NYC (Brooklyn/Queen) and NYU library. A person or a group of people can create, manage, schedule, and interact with others over their current library reads. The application can provided information about the public library’s location, and hours of operation (from the dataset: https://data.cityofnewyork.us/Recreation/BPL-Branches/xmzf-uf2w and https://data.cityofnewyork.us/Education/Queens-Library-Branches/kh3d-xhq7), which our users can utilize to organize their meeting times. Check Out can also present the various book clubs organized on the application for a particular library. Our application can be the launching point for established communities and newcomers to discuss their books in person and over our software. 

What is/are the problem/s you want to solve?

Reading is often thought of as a solitary activity and public libraries tend to be an underutilized resource. The project can bring people together to discuss their current reads and use what may be available to them in their community. NYU students will be able to organize book clubs (study groups) based on their interests and/or their studies. 

User Personas and Major Features

Who are the users you are targeting? 
Librarians - Advertising hours of operation for public/university libraries
Book club organizers - more active users (club admins)
Casual readers - ones to spectate and interact with existing clubs
NYU students - the university library will only be available to them

Who are the major features you are targeting? 
Viewing public and university libraries’ locations and details
Library page with hours of operation, address and list of hosted book clubs
User (login or simple username with email)
Book club memberships
NYU ID verification (https://wp.nyu.edu/developers/apis/) 
Book Club (user created)
Book Club Name, members, hosted library, current read, archived reads
NYU Libraries and limit availability to NYU students (via email validation)
Library page with hours of operation, address and list of hosted book clubs
Privatized Book clubs, invite only. 

MVP(Minimum Viable Product)
Which features are a must to have? (If you don't have these you do not have a project, not really)
The minimum viable product for our application would be the demonstration of libraries’ hours of operation and addresses, as well as the user’s ability to create an account and to create/subscribe (or unsubscribe) to book clubs for a particular library. The application should be able to show the book club’s current read and what time they meet at a library. Book club pages display the subscribers and meeting time.
MLP (Minimum Loveable Product)
Which features are a really nice to have to the users would fall in love with the product
Notification/email reminders for a book club meeting. 
Link to retrieve the book (link to library catalog). 
The ability to select the next book club pick. Voting poll.

Nice-To-Haves Features
Not MVP, not MLP but still would be cool do develop these features
Chat feature among the book club and/or user-to-user. 
Pick time to meet. Voting tool.
Display archived books for the club.
Online audio/video meeting capabilities. 
Transfer book club ownership. 
For NYU students only. Book room(s) at NYU libraries for book club.
For NYU students only. Optional to associate book club with course. 
Calendar display for book club subscriptions
When signing up for multiple book clubs, app will alert you of any conflicts. 

Call Out CRUD Features
How is this project interactive for the user personas?
C - create s
R - Read 
U - update information 
D - delete compost sites 

Admin - Librarian
UPDATE [PATCH] - library information, i.e. hours
DELETE - any library that is permanently closed 
CREATE [POST] - a book club hosted at a public library
UPDATE [PATCH] - meeting time
UPDATE [PATCH] - club name
UPDATE [PATCH] - club description
UPDATE [PATCH] - club’s current book pick
DELETE - book clubs 
READ - all book clubs information
[GET] club description 
[GET] club meeting time
[GET] club’s current book pick
[GET] list of subscribers
READ - all library information
[GET] library hours
[GET] library address
[GET] book club hosted at library

Persona 1 - NYU student
CREATE [POST] - an account (name and email)
UPDATE [PUT] - name
UPDATE [PUT] - email
CREATE [PUT] - subscribe/unsubscribe to club
CREATE [POST] - a book club hosted at 
an NYU library (only for NYU students) or a public library (available for all)
UPDATE [PATCH] - meeting time
UPDATE [PATCH] - club name
UPDATE [PATCH] - club description
UPDATE [PATCH] - club meeting time
UPDATE [PATCH] - club’s current book pick
DELETE - a book club they created or are admin of
READ - book club information
[GET] club description 
[GET] club meeting time
[GET] club’s current book pick
[GET] list of subscribers
READ - library information
[GET] library hours
[GET] library address
[GET] book club hosted at library

Persona 2 - Causal reader
CREATE [POST] - an account
UPDATE [PUT] - name
UPDATE [PUT] - email
UPDATE [PUT] - subscribe/unsubscribe to club
READ - book club information
[GET] club description 
[GET] club meeting time
[GET] club’s current book pick
[GET] list of subscribers
READ - library information
[GET] library hours
[GET] library address
[GET] book club hosted at library
Create invite links to others outside of the book club / application. 

Similar Already Existing

What similar applications exist on the market? (at least 3 with links and descriptions). 
If this work is truly unique and no one has even done anything even remotely similar please explain your search procedure and how you came to this conclusion

https://bookclubs.com/
BookClubs is an organization tool for readers to manage their club members and the book club picks.
https://bookmovement.com/bookclubapp/ allows readers to explore and review recommended books by book clubs, and also pick and vote for their favorite books 
https://www.goodreads.com/ 
Goodreads allows users to rate and write reviews on books that they are reading or anticipating. 
https://www.ourownbookclub.com/index.php
	Allows club members to discuss and interact over their reads online.



Account registration and management
A user should be able to create and manage an account for our application. The creation of an account will allow the user to interact with the libraries and book clubs. Without an account, a user would only be able to READ the library/book club information. 

	General User

As a general user, I want to be able to register for the application in order to interact with the rest of the features. Without an account, the user should only be able to view public libraries and book clubs. 
Acceptance criteria:  Collect name, valid email address, and password. OTP. Hash/salted password. User added to database. 
Acceptance tests:  Users can sign in and view the account page. Ability to subscribe (eventually implemented). User added to database.

As a general user, I want to be able to see all of my active subscriptions so that I may interact with them. 
Acceptance criteria: Collect which book clubs each person is subscribed to. User database should keep track of book club subscriptions.
Acceptance tests: Can show book clubs for each individual person. User database should keep track of book club subscriptions.

As a general user, I want to be able to update my account information so that the application is able to notify me. If it is an email change, then revalidate. If the password is changed, then hash/salt. 
Acceptance criteria:  Collect name, valid email address, and password. OTP. Hash/salted password. 
Acceptance tests:  Updated information must be stored in the database, must be tested with popular hashes. 

Casual Reader

As a casual reader, I want to be able to view libraries’ information and book clubs without having an account. 
Acceptance criteria: have libraries’ and book clubs details 
Acceptance tests: Able to view libraries’ details and book clubs 

	Library Admin
As a library administrator, I want to be able to see all the book clubs associated with my library.
Acceptance criteria:  collect all book clubs being created at specific libraries
Acceptance tests: For librarians they will have a separate page that shows all book clubs for the library they manage.

NYU Student
As an NYU student, I should be able to use my university email to access the university libraries on the application.  
Acceptance criteria:  NYU email.
Acceptance tests:  View university libraries only with an NYU email.

Library Information Management
The application should provide the detailed information about the NYC and NYU libraries available to our users. This information should include: library name, address, hours of operation, etc. Any user identified as a librarian should be able to update the library details and/or notify others of any changes. 

Developer

As a developer on the Check Out team, we need to condense the data of the public libraries from the following datasets on the Brooklyn and Queens boroughs (https://data.cityofnewyork.us/Recreation/BPL-Branches/xmzf-uf2w and https://data.cityofnewyork.us/Education/Queens-Library-Branches/kh3d-xhq7), as well as collect the information from all the NYU libraries. This data will be important to displaying to all of the library information in the application. 
Acceptance criteria:  One dataset with the name of the library, address, and hours of operations for every public library in Brooklyn and Queens, as well as the New York University libraries. 
Acceptance tests: 

Library Administrator 

As a library administrator, I want to be able to view and update my library’s details. To prevent accidental and unwanted updates, I would need to key in my password again for any changes made. 
Acceptance criteria:  have library details 
Acceptance tests: Librarians can edit library specific details in a special admin page

As a library administrator, I would like to notify all book clubs hosted at the library of any one time change in hours of operation. In the event of an emergency or inclement weather, the clubs would not have to meet at the library. 
Acceptance criteria: Emails/Text messages sent as notifications
Acceptance tests: all book clubs subscribers should receive the notification

Casual/General User

As a general reader, I want to be able to view the details of the library I am interested in. 
Acceptance criteria:  displaying map with all the libraries on it or list them in the UI by library name.
Acceptance tests: Able to see public libraries on a map, and able to see the list of libraries you have book clubs in.


Book Club Organization 
After creating an account, a user should be able to create a book club and/or interact (i.e. subscribe or unsubscribe) with already existing book clubs on our application. 

The professor expressed that the spirit should showcase the most convincing part of work. 
	
Book Club Organizer

As a book club organizer, I want to be able to create a book club hosted at a particular library so that others can join. In order to post the book club, I must enter the book club name, description, meeting time, hosting library, and current book club pick. 
Acceptance criteria: Valid inputs for all compulsory attributes listed
Acceptance tests: After a book club is created it is in the directory of clubs with the following information: book club name, description, meeting time, hosting library, and current book club pick

As a book club organizer, I want to be able to update any field in the book club I am the administrator of so that others are kept up to date and informed. I should be able to update any or all of the attributes at a time. 
Acceptance criteria: Valid inputs for each field e.g. meeting time should be within the opening hours of the relevant library.
Acceptance tests: The change is reflected in the database and user interface. 

As a book club organizer, I want to be able to delete a book club that I’m administrator of so that feeds are not noisy with inactive clubs. ???
Acceptance criteria: 
Acceptance tests: The change is reflected in the database and user interface. 

As a book club organizer, I want to be able to assign administrative rights of a book club that I’m administrator of to another user (can be a non-subscriber).
Acceptance criteria:  The database table with the book clubs should include the administrator and update it when necessary. 
Acceptance tests: 

As a book club organizer, I want to ensure that I would not be able to remove myself as the administrator of the book club if there are no other administrators.
Acceptance criteria: have a list of people in the book club
Acceptance tests: Give a warning to the book club organizer that notify them there is no one in the club if they leave

As a book club organizer, I want to be able to view and update weekly/monthly book selections of my book club. 
Acceptance criteria: Keep track of which book each book club is reading. 
Acceptance tests:  Book club organizers are allowed to change the book of the club but no one else.

As a book club organizer, I would like to notify the club of any meeting cancellation. In the event of an emergency or inclement weather, the club would not have to meet at the library. 
Acceptance criteria: 
Acceptance tests: 

As a book club organizer, I would like the option to privatize my book club so that the book club information is not pulized to everyone on the application. 
Acceptance criteria:  The book should not be included on the library page. The book club should only be available to subscribers via UI. 
Acceptance tests:  


Casual/General User

As a general user, I would like to see/read all available book clubs hosted at a particular library so that I can subscribe to any of the ones I find interesting. 
Acceptance criteria:  collect list of all books read for the book club
Acceptance tests:  Anyone can view the list of books the book club reads in  club details

As a general reader, I want to be able to accept or decline the assignment of the admin role of a book club. If I accept the role while I am not a current member, I will automatically be subscribed.
Acceptance criteria: Keep track of who is admin in the book club
Acceptance tests: Popup alert asking whether to accept role of admin

As a general reader, I want to be able to view my book clubs’ weekly/monthly pick. 
Acceptance criteria:  keep track of book picked for each club
Acceptance tests: When you see the list of book clubs you are able to see which book is currently being read

As a general reader, I want to be notified of my book clubs’ weekly/monthly selections every time it is updated. 
Acceptance criteria:  Email notification of updated information.
Acceptance tests: Email sent through some email service .

As a casual reader, I want to be able to subscribe to any book club of my choice so that I’m kept up to date with the club. 
Acceptance criteria:  User is added to the book club subscriber list.
Acceptance tests:  

As a casual reader, I want to be able to unsubscribe from any book club that I’m no longer interested in so that my feed is not cluttered with notifications that don’t pertain to me. 
Acceptance criteria:  Removed user from subscriber list. Keep track of the list of subscribers for the book club.
Acceptance tests:  User is no longer included in the subscriber list. Ability to remove oneself from the list of subscribers of a book club on profile page.

As a general user, I would like to turn off information notifications for specific clubs so that I am not disturbed.
Acceptance Criteria: no longer receive notifications for those specific clubs but can still receive notifications from other clubs
Acceptance Test: check if user still receives notifications when those clubs send one 

As a general user, I would like to see the archived list of previous book club picks. 
Acceptance Criteria:Keep track of the list of books for each club 
Acceptance Test:when looking at club information pull up the list of books the club already read.


Library Administrator 

As a library administrator, I want to be able to see all the book clubs associated with my library.
Acceptance criteria: Book clubs for each library are saved in database
Acceptance tests: in the librarian account, you can see the list of all book clubs

As a library administrator, I want to be able to modify or delete any book club associated with my library so that they are in line with the library’s regulations.
Acceptance criteria: save book club data in database
Acceptance tests: Changes are reflected in both interface and database

NYU Student Organizer

As a NYU student, I want to be able to create a book club hosted at any one of the NYU libraries. 
Acceptance criteria:keep track of nyu specific library
Acceptance tests:any nyu account should be able to make a book club when they select the library

Connecting Users
After creating an account, a user should be able to socialize on our application. The detailed features will make our application stand out and more immersive. 

As a book club organizer, I want to be able to make chat-wide announcements to all subscribers. 
Acceptance criteria: Chat functionality for book club
Acceptance tests: Message will be pinned at the top of the chat

As a book club organizer, I want to be able to remove members from the chat if they are not adhering to the guidelines. 
Acceptance criteria:  delete a member from the subscriber list and deleted member cannot resubscribe 
Acceptance tests: removed members are deleted from the subscriber list in the interface and also in the database

As a general reader, I want to be able to connect to other members of the same book club via a group chat.
Acceptance criteria: ability to message in the group chat
Acceptance tests: able to send and receive messages

As a librarian I want to be able to broadcast a message to all book club groups of an important message
Acceptance criteria: Chat functionality for book club 
Acceptance test: Message will appear in book clubs for the library the librarian manages with special text that specifies that it is from the librarian.



 

