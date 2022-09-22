'''This file is used in the Replit/Github tutorial on the D2I website. The aim is to provide a
simple task that will get users familiar with how to make changes to code on the D2I Github 
repos and start collaborating and writing validation rules. The goal of the task is to get this 
code from the D2I Github into your Replit, add your name and LA to the dictionary below, run 
the file to check it works, then commit it back to the repo, ready to be merged by someone from
D2I.'''

users = {
  'John Whitfield': 'Cheshire West and Chester LA',
  'Tracy Bell': 'Durham LA',
  'Gavin Burrell':'Durham LA',
  'Will Levack-Payne':'Data 2 Insight',
  'John Foster': 'Data 2 Insight',
  'Fake Analyst': 'Imaginary LA',
  'Tina Szabo': 'Wigan LA',
  'Jennifer Cook': 'Cheshire West and Chester',
  'Alistair Herbert': 'Data 2 Insight',
  'Phil Deakin': 'Manchester City Council',
}

for key in users:
  print('Name: ' + key + ', ' + 'LA: ' + users[key])
