Railway Reservation System:-
A Python CLI application designed to manage train passenger bookings, calculate compartment fares, generate formatted e-tickets, and perform search, analysis, and ticket cancellation operations.

Features:-
Passenger Booking: Enter passenger details including PNR ID, Name, Sex/Gender, Compartment Class, Source, and Destination.
Dynamic Fare Calculation: Automatically determines ticket pricing based on selected class/compartment.
Search Capabilities:Search passenger records by Passenger ID (PNR).Identify the passenger who paid the highest ticket fare.
Fare Analytics: Compute and display the average fare across all registered passengers.
E-Ticket Generation: Render ASCII formatted Indian Railways e-tickets directly to the terminal.
Ticket Management:Add additional passenger entries iteratively.Cancel existing tickets by Passenger ID with automatic refreshed ticket generation.

Compartment Pricing Chart
Compartment Class        Fare (₹)
general                  ₹2,500
AC 1 TIER                ₹3,200
AC 2 TIER                ₹3,500
AC 3 TIER                ₹3,700

Getting Started
Prerequisites
      Python 3.x installed on your system.
Running the Application
Save the code into a Python file (e.g., railway_reservation.py).
Open your terminal or command prompt.
Run the script:     python railway_reservation.py


Usage Walkthrough:-
Initial Entry: Enter the initial number of passengers to register.
Passenger Input: Provide PNR ID, name, gender, class (general, AC 1 TIER, AC 2 TIER, or AC 3 TIER), source station, and destination.
Search & Analytics:
                  Confirm with Y when prompted to search for specific passenger details using PNR                         ID.Confirm with Y to retrieve highest-paid passenger details.Confirm with Y to view                     average fare calculations.
Append Bookings: Enter Y to iteratively add single passenger bookings.
Print E-Tickets: Enter Y to generate formatted e-tickets.
Ticket Cancellation: Enter Y followed by the Passenger PNR ID to remove a record and update ticket printouts.


Data Structure:-
Passenger records are dynamically managed in a 2D Python list (main), structured as follows:
[PNR_ID, Name, Sex, Compartment, Source, Destination, Fare]


Sample E-Ticket Output
+========================================================================================+
|                                INDIAN RAILWAYS E-TICKET                                |
+========================================================================================+
| PNR NUMBER: 102938                            | BOOKING TIME: 2026-09-23 19:14:53     |
+========================================================================================+
| TRAIN: 12424 - Rajdhani Express               | CLASS: AC 2 TIER                       |
| FROM: New Delhi                               | TO:  Mumbai Central                    |
+========================================================================================+
| PASSENGER DETAILS:                                                                     |
| Name: Alex Vance                              | Age/Sex: Male                          |
+========================================================================================+
| STATUS: CONFIRMED                                                                      |
| COACH: A5           | SEAT: 5                             | PRICE : 3500       |
+========================================================================================+
|                       *** WISHING YOU A SAFE AND HAPPY JOURNEY ***                      |
+========================================================================================+
