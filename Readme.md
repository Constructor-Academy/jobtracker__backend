# JobTracker - Backend

Welcome to **JobTracker Backend**! The ultimate solution to organizing and keeping tabs on your job applications. Don't let opportunities slip through the cracks - visualize and manage the statuses of your job pursuits with ease.

[![Demo Video](https://img.youtube.com/vi/Xx_BwZ6RqHg/0.jpg)](https://www.youtube.com/watch?v=Xx_BwZ6RqHg)

^ Click to watch the demo video ^

## 🚀 Features

- **Organized Kanban Board**: View all your job applications in a streamlined drag&drop interface.
- **Status Tracking**: Update and monitor the current state of each application - from 'Wishlist' to 'Interview' to 'Accepted' and everything in-between.
- **Instant Access**: Dive deep into each job detail with just a few clicks.

🌐 [**Live Application**](https://jobtracker.ai/)

## 📖 About this Repository

You're currently viewing a snapshot from the JobTracker Backend private repository, as of July 2023. This version is open-sourced to provide transparency, share knowledge, and invite collaboration from the developer community.

The Frontend code can be found [here](https://github.com/Constructor-Academy/jobtracker__frontend).

> This project is not under very active development and most of the packages are outdated and would need an update.

## 🚀 Getting Started

1. Clone the Repository

   ```bash
   git clone https://github.com/Constructor-Academy/jobtracker__backend
   cd jobtracker-backend
   ```

2. Build Docker Image

   ```bash
   docker build -t "jobtracker-backend" .
   ```

3. Setup Environment Variables 
   - Duplicate the .env.template file and rename it to dev.env.
   - Inside dev.env, fill in the required secrets. Remember, this file is git-ignored, ensuring your secrets stay safe:
     - Essential: postgres, django_debug, secret_key 
     - Email Configuration (for sending out notifications): If left unset, the project runs, but no emails will be sent.
     - Sentry Integration: sentry_dsn is needed only if you plan to use Sentry for error tracking.

4. Start Docker Containers

   ```bash
   docker compose up -d
   ```
   
5. Run Initial Backend Setup
   - Access the Django backend container:
     ```bash
     docker exec -ti jobtracker-django bash
     ```

   - Apply migrations:
     ```bash
     python manage.py migrate
     ```
   
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
   
   - Start the development server:
     ```bash
     python manage.py runserver 0:8000
     ```
   
6. Verify Backend Installation
- Check API endpoints: http://localhost:8000/backend/api/docs/
- For email functionality during local development, whitelist your email: Visit http://localhost:8000/backend/admin/emails/devemails/ and add the email address you want to use to register. Only whitelisted addresses will receive emails.

🎉 That's it! With the backend ready, you can now run the frontend in parallel and start creating accounts via the UI.


- clone repo 
- docker build -t "jobtracker-backend" .
- copy the `.env.template` file and create a `dev.env` file. In `dev.env`, secrets can be added. This file will be ignored by git.
  - postgres, django_debug and secret_key variables are required
  - email is needed for emails to be sent out, but the project will also run without it
  - sentry_dsn is only required if you want to use sentry
- docker-compose up -d
- docker exec -ti jobtracker-django bash
- python manage.py migrate
- create a superuser with `python manage.py createsuperuser`
- python manage.py runserver 0:8000
- visit http://localhost:8000/backend/api/docs/ to see if it's running correctly and to discover the api endpoints
- visit http://localhost:8000/backend/admin/emails/devemails/ and add your email address you want to use to register *during local development / on localhost*. Only registered addresses will receive emails.

🎉 That's it! With the backend ready, you can now run the frontend in parallel and start creating accounts via the UI.
