# Django Task Management Project

This Django project is a simple task management application that allows users to create, manage, and summarize tasks. It provides functionalities to track the status and priority of tasks, as well as generate a summary report of tasks.

## Features

- **Task Creation**: Users can create tasks with a title, description, due date, and priority level.
- **Task Management**: Tasks can be marked as pending, completed, or canceled.
- **Admin Interface**: A user-friendly admin interface for managing tasks.
- **Task Summary**: A summary page that displays statistics about tasks, including totals by status and priority.

## Technologies Used

- Django
- postgreSQL
- HTML

## Installation

- Clone the repository:
- git clone https://github.com/mosisn/Task-Manager.git
- cd Task-Manager



### Create a virtual environment:
- python -m venv venv
- venv\Scripts\activate



### Install dependencies:
- pip install -r requirements.txt

### Create .env file:
- it should contain:
  - DATABASE_NAME
  - DATABASE_PASS
  - DATABASE_USER
  - DATABASE_HOST
  - DATABASE_PORT
  - SECRET_KEY
  - ALLOWED_HOSTS
  - DEBUG


### Run migrations:
- python manage.py migrate


### Create a superuser (for accessing the admin interface):
- python manage.py createsuperuser


### Run the development server:
- python manage.py runserver


### Access the application:
- Open your browser and go to http://127.0.0.1:8000/.
- Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## Usage

- **Adding Tasks**: Navigate to the admin panel to add new tasks.
- **Managing Tasks**: You can edit task statuses directly from the admin interface.
- **Viewing Summary**: Visit http://127.0.0.1:8000/task-summary/ to view a summary of all tasks.

## Task Model

The `Task` model includes the following fields:

- `title`: A string field for the task title.
- `description`: A text field for a detailed description of the task.
- `status`: A choice field to indicate the task's status (pending, completed, canceled).
- `due_date`: A DateTime field for the task's due date.
- `priority`: A choice field to set the task's priority (low, medium, high).
- `created_at`: A timestamp for when the task was created.
- `updated_at`: A timestamp for when the task was last updated.

## Admin Configuration

The admin interface is configured to allow:

- Filtering tasks by status and priority.
- Editing task statuses directly from the list view.
- Custom actions to mark tasks as completed, pending, or canceled.

## Summary View

The summary view provides insights into:

- Total number of tasks.
- Count of tasks by status (completed, pending, canceled).
- Count of overdue tasks.
- Count of tasks due today.
- Count of tasks created in the last week.
- Count of tasks categorized by priority.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.


## Acknowledgments

- Django documentation for guidance on building web applications.
- Open source community for inspiration and support.
- Chat GPT-4o mini which i used for faster writing of comments, documentation and debugging. 