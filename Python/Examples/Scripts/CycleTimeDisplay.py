# This example shows how to quickly calculate the cycle time of a program
#
# Important notes and tips for accurate cycle time calculation:
# https://robodk.com/doc/en/General.html#CycleTime

# Start the RoboDK API
from robodk.robolink import *  # RoboDK API

RDK = Robolink()

# Ask the user to select a program
program = RDK.ItemUserPick('Select a program', ITEM_TYPE_PROGRAM)
if not program.Valid():
    quit()

# Retrieve the robot linked to the selected program
robot = program.getLink(ITEM_TYPE_ROBOT)
if not robot.Valid():
    RDK.ShowMessage("Cycle time requires a robot to be linked to the program '" + program.Name() + "'. Right-click the program to link it.")
    quit()

# Output the linear speed, joint speed and time (separated by tabs)
writeline = "Program name\tProgram status (100%=OK)\tTravel length\tCycle Time"
print(writeline)
# Prepare an HTML message we can show to the user through the RoboDK API:
msg_html = "<table border=1><tr><td>" + writeline.replace('\t', '</td><td>') + "</td></tr>"

result = program.Update()
instructions, time, travel, ok, error = result

# Print the information
newline = "%s\t%.0f %%\t%.1f mm\t%.1f s" % (program.Name(), ok * 100, travel, time)
print(newline)
msg_html = msg_html + '<tr><td>' + newline.replace('\t', '</td><td>') + '</td></tr>'

msg_html = msg_html + '</table>'

RDK.ShowMessage(msg_html)
