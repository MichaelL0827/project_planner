# Overview

This is an attempt at making a multi-person web app planer. Like the scheduled events in you Google Calendar you can schedule a date and time for the event, then on top of it, add todo items to the event. Then you can add your friends or associates to the event and they can mark off todo items when they have them complete. (e.g. Camping trip needs 1 cooler for drinks, a friend could mark that off as being completed by them.)

In planning your parties outings or even group projects it's difficult to keep track of what needs to be done where there are multiple parties involved, so this app is being developed to make the group planning and execution easier.

# Development Environment

We started off trying to develop using .NET MAUI, but found that developing using it requires a lot of pices coming together to make it happen. You need the same version of the SDK, and the same version of the program, then in order to link it together using github everyone needs to have the same version otherwise they won't be able to pull and push from the repository. Other tools involved using fastAPI and mySQL to manage the multi-person aspect of the project. FastAPI calls to the SQL Database and manages the requests made on the front end.

# Useful Websites

* https://dotnet.microsoft.com/en-us/apps/maui
* https://devdocs.io/fastapi/

# Future Work

* Add connectivity with Front and backend files for full functionallity
* Include push notifications to alert users when an event is coming up or a todo item is updated.
* Include cheese in the code for those sneaky enough to look at it so they get a treat.