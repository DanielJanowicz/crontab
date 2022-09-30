# Here are the steps to setup an automation for pulling data from an API to be stored locally

### Initial VM setup
1. Boot up your virtual machine & connect to it via terminal/command prompt
2. Update your virtual machine with:
> $ sudo apt-get update
3. Ensure crontab is installed via crontab -h
4. Cntrl/Cmd X to close the window
5. Install nano:
> $ sudo apt-get install nano
6. Select nano as the editor:
> $ select-editor
> *select nano*

### Importing files
1. Import your files from github:
> $ git clone https://github.com/userName/repoName (Example)
2. Enter the directory of the repo
3. (Optional) Make last minute adjustments to .py files:
> nano fileName.py

### Enabling crontab
1. Open crontab
> $ crontab -e
2. Provide crontab time/date format (refer to crontab.md)
3. Provide location to file on the same line
4. Save & close

### Creating a Bash
1. Create the script
> $ nano auto.sh
> *#1/bn/bash*
> /location/of/python3 /location/to/python/file/pythonFile.py
2. Provide higher privledges
> $ chmod +x auto.sh
3. Run the script (will loop)
> $ ./auto.sh

---

Viewable logs & datafiles will prove the system is operating