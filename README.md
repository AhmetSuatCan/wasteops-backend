# WasteOps Backend

WasteOps is a waste management system designed to help municipalities and related organizations efficiently coordinate their waste collection operations. The system enables features such as team creation, task assignment, route planning, and shift scheduling — all tailored to different user roles like Admins and Employees. This repository contains the backend codebase built with Django and Django REST Framework.

---

## 🚀 Project Overview

WasteOps allows organizations to:
- Create and manage their own teams and staff.
- Define and manage waste collection vehicles and facilities.
- Design waste collection routes.
- Assign shifts and tasks to teams based on routes.
- Authenticate and authorize users with different roles (Admin, Manager, Team Chief, Personnel).

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Django** – High-level Python web framework.
- **Django REST Framework** – API development.
- **PostgreSQL** – Relational database system used for structured data.
- **JWT Authentication** – Token-based secure authentication using [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).
- **Leaflet.js Integration (TODO)** – For interactive route creation and mapping.

---
## 🏗️ Project Architecture

The project follows a modular app-based structure using Django best practices:\

wasteops-backend/
├── apps/
│ ├── human_resources/ # Team creation and personnel management
│ ├── organization/ # Organization-level data and inventory management
│ ├── users/ # Authentication and user roles (Admin / Employee)
│ ├── operations/ # (TODO) Task assignment, shift planning
│ └── map_routes/ # (TODO) Route creation and map integrations
├── config/ # Django settings, environment configs, main URLs
├── manage.py # Project entry point
├── requirements.txt # Python dependencies

## 📦 Apps Description

### `users/`
Handles authentication and user management. Supports role-based access for Admins and Employees. Includes endpoints for:
- Registration / Login
- Token-based authentication
- Role-based permissions

### `organization/`
Allows creation of organizations and their internal resources. Manages:
- Inventory (vehicles, containers)
- Facilities (e.g. recycling centers, waste stations)

### `human_resources/`
Connects personnel with organizations. Manages:
- Teams and team chiefs
- Employee assignments
- Staff directory

### `operations/` (Coming Soon)
Will handle:
- Task scheduling
- Shift planning
- Attaching teams to shifts and routes

### `map_routes/` (Coming Soon)
Will integrate with **Leaflet.js** to support:
- Drawing custom routes
- Assigning routes to teams and shifts
- Route optimization support (future)

---

## 📄 Setup Instructions (Coming Soon)

Instructions for installing dependencies, setting up the database, and running the development server will be added as the project progresses.
