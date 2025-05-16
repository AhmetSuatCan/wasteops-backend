
---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Django** – High-level Python web framework.
- **Django REST Framework** – API development.
- **PostgreSQL** – Relational database system used for structured data.
- **JWT Authentication** – Token-based secure authentication using [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).
- **Leaflet.js Integration (TODO)** – For interactive route creation and mapping.

---

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
