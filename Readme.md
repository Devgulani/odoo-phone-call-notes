# Phone Call Notes

An Odoo 18 custom module that enables sales teams to log and manage customer phone calls directly from the Contacts application.

This project was developed as part of the Odoo Developer Internship Technical Assessment for ZantaTech Solutions.

## Features

- Log customer phone calls
- Store call details including:
  - Customer
  - Phone Number
  - Call Status
  - Notes
  - User
  - Call Date
- Contact integration with Odoo Contacts
- Smart Button showing the number of call logs for each contact
- View complete call history for each customer
- Tree View
- Form View
- Search View
- Internal User access control

## Tech Stack

- Odoo 18 Community
- Python 3.12
- PostgreSQL 17
- XML
- Odoo ORM

## Module Structure

```
phone_call_notes/
│
├── models/
│   ├── phone_call_log.py
│   └── res_partner.py
│
├── security/
│   └── ir.model.access.csv
│
├── views/
│   ├── phone_call_log_views.xml
│   └── res_partner_views.xml
│
├── __init__.py
├── __manifest__.py
```

## Installation

1. Copy the module into your `custom_addons` directory.

2. Add the directory to `addons_path` in `odoo.conf`.

3. Restart the Odoo server.

4. Update the Apps List.

5. Install **Phone Call Notes** from the Apps menu.

## Usage

1. Open **Contacts**.
2. Select any customer.
3. Manage customer call logs directly from the Contact form using the integrated Call Logs Smart Button.
4. Create and manage customer call records.
5. View the complete call history for each contact.

## Future Improvements

- Log Call popup (wizard)
- Twilio integration
- Kanban View
- Call recording support
- Dashboard and reporting
- Advanced filters

## Author

**Deepak Gulani**

GitHub: https://github.com/Devgulani
Linkedin: https://www.linkedin.com/in/deepak-gulani-a77b37298/

---

Developed using Odoo's ORM, XML Views, and Security framework while following standard Odoo module development practices.