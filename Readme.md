# Phone Call Notes

A custom Odoo 18 module that enables sales teams to log and manage customer phone calls directly from the Contacts module.

## Features

- Log customer phone calls.
- Store:
  - Customer
  - Phone Number
  - Call Status
  - Notes
  - User
  - Call Date
- View all call logs in a dedicated menu.
- Smart Button on the Contact form displaying the total number of calls.
- Open all call logs for a contact directly from the Smart Button.
- Search and filter call logs.
- Automatic user and date tracking.

## Bonus Feature

### Quick Call Wizard

A **Call** button is available directly on the Contact form.

Instead of navigating to the Phone Call Logs menu, users can:

1. Open a popup wizard.
2. Select the call status.
3. Enter call notes.
4. Save the call.

The wizard automatically creates a Phone Call Log linked to the selected contact and updates the Smart Button count.

## Module Structure

```
phone_call_notes/
├── models/
│   ├── phone_call_log.py
│   └── res_partner.py
├── wizard/
│   ├── phone_call_wizard.py
│   └── phone_call_wizard_views.xml
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── phone_call_log_views.xml
│   └── res_partner_views.xml
├── __manifest__.py
└── README.md
```

## Installation

1. Copy the module into the `custom_addons` directory.
2. Add the folder to `addons_path` in `odoo.conf`.
3. Restart the Odoo server.
4. Update the Apps List.
5. Install **Phone Call Notes**.

Or update the module using:

```bash
python odoo-bin -c ..\odoo.conf -u phone_call_notes -d odoo18
```

## Usage

### Method 1 – Phone Call Logs Menu

- Open **Phone Call Logs**.
- Create a new call log.
- Select the customer.
- Fill in the call details.
- Save.

### Method 2 – Contact Smart Button

- Open a Contact.
- Click **Call Logs**.
- View all call logs related to that contact.

### Method 3 – Quick Call Wizard (Bonus)

- Open a Contact.
- Click **Call**.
- Select the call status.
- Add notes.
- Click **Save**.

A new Phone Call Log is automatically created for that contact.

## Technologies Used

- Odoo 18
- Python
- PostgreSQL
- XML
- Odoo ORM

## Assignment Requirements Covered

- ✅ Custom Model
- ✅ ORM Relationships
- ✅ Form View
- ✅ Tree/List View
- ✅ Search View
- ✅ Menu & Action
- ✅ Security Access Rules
- ✅ Contacts Integration
- ✅ Smart Button
- ✅ Contact-specific Call History
- ✅ Bonus Call Wizard

## Author

**Deepak Gulani**

GitHub: https://github.com/Devgulani