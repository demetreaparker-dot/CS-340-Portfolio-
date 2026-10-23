# CS 340 – Client/Server Development

## Project Two: Grazioso Salvare Rescue Animal Dashboard

For my CS 340 portfolio submission, I selected my Grazioso Salvare Rescue Animal Dashboard. This project demonstrates my experience using Python, MongoDB, and Dash to develop an interactive application that retrieves, filters, and visualizes animal shelter data.

The dashboard allows users to identify dogs that may be suitable for water rescue, mountain or wilderness rescue, and disaster or individual tracking. It includes an interactive data table, filtering controls, a breed distribution chart, and a geolocation map.

## How Do I Write Programs That Are Maintainable, Readable, and Adaptable?

I believe writing maintainable and readable programs starts with keeping the code organized and separating different responsibilities. Throughout this course, I learned how important it is to create code that can be reused instead of writing the same functionality multiple times.

One example was the CRUD Python module I developed in Project One. Rather than writing all my MongoDB connection and query code directly inside the dashboard, I created a separate module to handle database operations. This made my Project Two dashboard easier to manage because the interface could focus on displaying information while the CRUD module handled communication with MongoDB.

Another advantage was that I could troubleshoot the database connection without having to change the entire dashboard. In the future, I could reuse this module in other Python applications that need to store, retrieve, update, or delete MongoDB records. I would only need to adjust the database configuration and queries to match the new project's requirements.

## How Do I Approach a Problem as a Computer Scientist?

When approaching a programming problem, I like to break it down into smaller tasks and work through each part before moving on to the next. This approach was especially helpful during the Grazioso Salvare project because the assignment involved multiple technologies that needed to work together.

I started by making sure my MongoDB database was configured correctly and that my CRUD Python module could retrieve the animal records. After confirming the database connection, I worked on the dashboard layout, rescue filters, data table, and visualizations.

One challenge I encountered involved MongoDB authentication. I had to identify the correct authentication database before my Python application could connect successfully. I also experienced issues displaying the dashboard in JupyterLab, which required me to adjust how the application was launched.

Compared with some of my previous programming assignments, this project required more attention to how different components communicated with one another. Instead of focusing only on writing a single program, I had to consider the database, Python module, user interface, and interactive features as parts of one application.

In the future, I would continue using this step-by-step approach. I would begin by understanding the client's requirements, designing the database structure, testing queries, and then developing the application around those requirements.

## What Do Computer Scientists Do, and Why Does It Matter?

Computer scientists solve problems by designing, developing, and improving software and technology. Their work helps individuals and organizations manage information, automate tasks, and make better decisions.

The Grazioso Salvare project is a good example of how computer science can support an organization's goals. The dashboard helps users search through animal shelter records and identify dogs that meet specific rescue training requirements. Instead of manually reviewing thousands of records, users can apply filters and quickly narrow the results.

The data table, breed distribution chart, and geolocation map also make the information easier to understand. These features could help an organization like Grazioso Salvare save time and make more informed decisions when identifying potential rescue animals.

This project helped me understand that software development is not just about writing code. It is also about creating solutions that are useful, reliable, and easier for people to work with.

## Final Reflection

Overall, CS 340 helped me strengthen my knowledge of database systems and Python application development. I especially enjoyed working with MongoDB and seeing how database queries could be connected to an interactive dashboard.

I also learned the importance of reusable code, troubleshooting, and testing individual components before combining them into a complete application.

As I continue working toward my computer science degree, I plan to build on these skills and apply them to future software engineering and database development projects.

## AI Assistance Acknowledgment

I used ChatGPT (OpenAI) to assist with troubleshooting Python and MongoDB code, understanding dashboard requirements, and drafting portions of my project documentation and portfolio reflection. I reviewed and tested the application in my development environment.
