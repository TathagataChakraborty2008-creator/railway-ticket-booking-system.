# Railway Ticket Booking & Management System is

A Python terminal-based program designed to book tickets, search passenger data, calculate ticket analytics, display styled Indian Railways e-tickets, and process ticket cancellations.

---

## Features are

- **Passenger Booking:** Registers passenger details including PNR ID, Name, Sex, Compartment/Class, Source, Destination, and Fare.
- **Passenger Search:** Finds and displays passenger details using their PNR / Passenger ID.
- **Fare Analytics:**
  - **Highest Fare Finder:** Identifies the passenger who paid the maximum fare amount.
  - **Average Fare Calculator:** Computes the average fare price across all booked tickets.
- **E-Ticket Generation:** Prints formatted e-tickets aligned within customized borders for terminal viewing.
- **Ticket Cancellation:** Cancels booked tickets by Passenger ID and updates active e-tickets in real time.
- **Interactive Data Entry:** Prompts users to dynamically add extra passenger entries prior to printing tickets.

---

## Requirements are:=

- **Python 3.x** (Uses built-in Python libraries; no external dependencies required).

---

## Data Schema (`main` List Structure)

Passenger records are stored as nested lists within a central `main` list structured as follows:

| Index | Field | Description |
| :--- | :--- | :--- |
| `[0]` | `pnr` | Passenger ID / PNR Number |
| `[1]` | `name` | Passenger Full Name |
| `[2]` | `sex` | Sex / Gender / Age details |
| `[3]` | `com` | Compartment (`general`, `AC 1 TIER`, `AC 2 TIER`, `AC 3 TIER`) |
| `[4]` | `sourse` | Origin / Starting Station |
| `[5]` | `des` | Destination Station |
| `[6]` | `fare` | Ticket Price (Integer) |

---

## Functions Overview

### 1. `data_enter(n)`
Captures inputs for `n` passengers, builds individual passenger lists, and appends them to `main`.

### 2. `search_data(ask)`
Prompts for a Passenger ID and prints matching passenger details if found in `main`.

### 3. `serch_data(askhighstfair)`
Scans all entries to locate and display details for the passenger paying the highest fare value.

### 4. `average_fair(avgfair)`
Sums up ticket fares for all active records and prints the overall average fare.

### 5. `my_ticket()`
Renders styled, bordered Indian Railways E-Tickets in the terminal for every booked passenger.

### 6. `cancelticket(z)`
Removes a is  record matching PNR id /Passenger ID `z` from `main` and re-prints remaining valid tickets.

---

## How to Run the code

1. Copy the Python script into a file named `railway_booking.py`.
2. Open terminal/command prompt in the directory containing the file.
3. Run the application:

```bash'''
python railway_booking.py
