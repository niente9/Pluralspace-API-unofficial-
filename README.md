# PluralSpace-API-unofficial-
Source code for unofficial third-party API for PluralSpace. Displays name, ID, color, avatar URL, description, message prefix, and custom fields of current fronter(s) and current member.

Though the program asks for the email and password to sign in to PluralSpace, it does not store the information permanently. It simply sends the information to PluralSpace servers in an encrypted request to sign in.

Estimated execution time: 1.5 seconds + 1 second per fronter (I had to add a delay to not overload the PluralSpace servers)

Required PyPI packages: requests, bs4, lxml

I have no affiliation with the developers of PluralSpace.

This is my first project in python, so it is likely not well optimized. AI was not used to code this.
