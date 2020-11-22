# Job_Hunt

This is a script to automate and scrapp jobs from indeed' worldwide site 

# How to run this script  :
   - open terminal , install from requirements.txt, i use pipenv to create virtualenv for my projects.
   
   -  better to delete the two Pipfiles, and re-run pipenv install -r requiremens.txt to re-generate the two files again and create venv for the project.
  
  - run,  python Job_Scrapper.py
  
  # Terminal input: 
  - Provide one of the numbers listed on locations.json file
    - I used auto incremented ids to avoid typing the whole location, check for id of the location you want and thene type it.
    
  - Feel free to leave one of these inputs empty, but not both
    - Provide city in which you want to search for jobs in
    - Provide what job you're looking for
    
  - The Script will continue automaticly, and change the sorting type to (Last 7 days).
  - Jobs Scrapped will be saved to .json file 
  
  ### This script can always be enhanced and modified, feel free to fork it and make changes !!
