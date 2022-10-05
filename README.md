# System-Integration-Mini-Project-2


## Documentation


First off, i would like to specify that i personally feel that the requirements for this assignment were unclear. I am unsure what is expected, but tried to create something that fulfills the following requirements:

1. Create a small system that can handle user complaints.
2. Implement a message broker or a message queue.
3. There has to be some aspect of automatisation.
4. Create a diagram using Camunda.


The entire system runs in a contained docker container. The setup of the system is therefore relatively easy, however the "e-mail" aspect is a bit hostile. I don't know if a there is a better alternative, but i personally setup two emails using googles g-mail api, in order to send and receive emails. In order to use the system fully, one would have to create 2 emails via googles api, allow both of these emails to be used by "unauthorized" applications, and then put both these emails in an enviroment file, under the tags "RECEIVER_COOPERATE_EMAIL" and "SENDER_COOPERATE_EMAIL". When using the google g-mail api, you are always giving a "credentials" file. This will also have to be put at the root of the system.

<img width="119" alt="Screenshot 2022-10-05 at 14 59 22" src="https://user-images.githubusercontent.com/56427491/194066167-f58dc12d-b452-4c35-babe-6b1d7fc34c89.png">

Due to this fact, i wouldn't recommend trying to use the system, which is obviously poor developing by me.

Using "docker-compose build . && docker-compose up -d", The Docker builds the codebase along with all the libraries listed in "requirements.txt".

Upon starting the system, microservice1 and microservice2, are booted up.

Microservice1 deals with allowing users to send their complaints.

<img width="915" alt="Screenshot 2022-10-05 at 15 05 12" src="https://user-images.githubusercontent.com/56427491/194067264-32381cf8-5f6f-4ba3-9db1-0f9b40b7f914.png">

To state the obvious, there is no frontend, but essentially the user types in their email, the subject of the complaint, and then the actual complaint.
The email is verifed to check if it exsists or not, and the subject and complaint get sanitized as to prevent various attacks.
If all looks good, they are greeted with an auto-reply message.


The complaint is then send to Redis. The idea here being that instead of a complaint going directly to the company email, we wait for more complaints to pile up before we send them. So Redis acts as our message queue.


Microservice2 has the job of dequeueing these messages and sending them to the company email. This occurs automatically every morning at 5:00. A cron job has been created to ensure this. 


<img width="332" alt="Screenshot 2022-10-05 at 15 14 45" src="https://user-images.githubusercontent.com/56427491/194069215-6e16e13d-8282-4e05-8bd8-a7dfe011f2f4.png">



And finally this is what it looks like when a complaint has landed at the cooperate e-mail.
<img width="1055" alt="Screenshot 2022-10-05 at 15 16 08" src="https://user-images.githubusercontent.com/56427491/194069510-63aa2628-fcd5-4b09-9094-54d87900403d.png">

From here it is a manual process for the company to look at a complaint and respond to the user.


## Own thoughts
This assignment was a bit of a rush job. There are a lot of things that could have been done better, and quite frankly should have been done better.
I am not all that satisfied with how it turned out, but it is what it is. Originally the system was supposed to be bigger and could handle different types of complaints and send them to different departments, but i forgot all about the assignment and had to create a light version of that idea. I am also very unsure if i had to use Camunda or not and what purposed it served.


