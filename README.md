# Employee Leave Balance Tracker 👨‍💼

A Django-based system for tracking employee work hours and automatically deducting vacation/leave balance based on accumulated hours.

## 📋 Overview

This project tracks how many hours an employee works. Whenever an employee accumulates **6 hours**, it counts as **one full working day**, and that day is automatically **deducted from the employee's vacation/leave balance. This automates what would otherwise be a manual HR calculation.

## ✨ Features

- **Add Employee**: Create new employee records through a simple form.
- **Search Employee**: Search employees by name using `icontains` lookup (partial match, case-insensitive).
- **Edit Employee**: Update employee data with automatic leave balance recalculation.
- **Automatic Hour-to-Day Conversion**: Every time an employee's hour count (`emp_hour_no`) reaches `6`, the system treats it as **one full day worked**, decreases `emp_balance` (vacation/leave balance) by `1`, and resets the hour counter back to `0`.
- **Read-only Fields**: Sensitive fields (`emp_no`, `emp_name`, `emp_balance`) are set to read-only in the edit form to prevent manual tampering, since the balance should only change through the automated hour-tracking logic.
- **Auto Timestamps**: `emp_date_update` field updates automatically on every save using `auto_now=True`.

## 🗂️ Project Structure

```
emp_info/
├── models.py       # Emp_info model definition
├── forms.py        # ModelForm with custom widgets
├── views.py        # Core views: search, add, edit
├── utils.py        # Business logic for balance calculation
└── templates/
    └── pages/
        ├── search_p.html
        ├── add_p.html
        └── edit_p.html
```

## 🧱 Model Fields

| Field | Type | Description |
|---|---|---|
| `emp_no` | IntegerField | Employee number |
| `emp_name` | CharField | Employee name |
| `emp_balance` | IntegerField | Employee's remaining vacation/leave balance (in days) |
| `emp_hour_no` | IntegerField | Accumulated work hours; resets every 6 hours (= 1 day) |
| `emp_date_created` | DateField | Date the employee record was created |
| `emp_date_update` | DateField (auto_now) | Last time the record was updated |

## ⚙️ Hour-to-Day / Leave Balance Logic

The core business logic lives in `utils.py`:

```python
def update_emp_info(emp_id, hour_no, balance):
    if hour_no == 6:
        balance -= 1
        hour_no = 0
        emp_id.emp_balance = balance
        emp_id.emp_hour_no = hour_no
        emp_id.save()
```

**How it works:**

Whenever an employee's `emp_hour_no` reaches `6` hours:
1. It's counted as **1 full working day**.
2. `emp_balance` (vacation/leave balance) is decreased by `1` day.
3. `emp_hour_no` resets back to `0` to start counting the next day.
4. The updated record is saved.

This means `emp_balance` represents **how many vacation days the employee has left**, and it decreases automatically as they accumulate work hours — no manual HR intervention needed.

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite (default, can be changed)
- **Frontend**: Django Templates + HTML

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Django

### Installation

```bash
# Clone the repository
git clone https://github.com/Firas-coder/<repo-name>.git
cd <repo-name>

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` in your browser.

## 📌 Notes

- The `edit_fun` view retrieves the employee, validates and saves the form, then calls `update_emp_info` to apply the hour-to-day conversion and update the leave balance.
- The `search_fun` view returns all employees by default, or filters by name when a search query is provided via GET.
- `emp_balance` should be treated as a **read-only value from the user's perspective** — it's meant to be updated only through the automated hour-tracking logic, not edited manually.

## 📝 License

This project is open source and available for learning and personal use.

---

Made with ❤️ using Django
