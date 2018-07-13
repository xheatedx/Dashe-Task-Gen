# Dashe-Task-Gen

Quickly generates tasksk json for Dashe with custom keywords for one or multiple sites at once

1. Fill in profiles.txt with your Dashe profiles exactly how they are on your Dashe. One per line.

2. Adjust sizes.txt to your preferences one per line. Gen runs through sizes sequentially.

3. If running Undefeated replace filler accounts in logins_undftd.txt with your logins. Tasks will cycle through this list.
If not running Undefeated still leave dummy accounts there they will not affect tasks as useAccount is set to False when 
not running Undefeated. One account per line in this format undftd@gmail.com:Password123

Run script and tasks will be generated to Generated Tasks.json. Import that file into Dashe and that's it.

@chexmdc

