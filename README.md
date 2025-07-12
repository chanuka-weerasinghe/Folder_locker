\# Folder Locker



A Python script that provides basic folder protection on Windows systems using file system operations and Windows commands.



\## Features



\- \*\*Rename Protection\*\*: Renames folders with password suffix

\- \*\*Hide Folder\*\*: Uses Windows `attrib` command to hide folders

\- \*\*Permission Control\*\*: Removes user access permissions (requires admin rights)

\- \*\*Simple Interface\*\*: Easy lock/unlock commands



\## Requirements



\- Windows OS

\- Python 3.x

\- Administrator privileges (recommended for full protection)



\## Usage



1\. \*\*Create a folder\*\* manually (e.g., `TestFolder` on Desktop, or your file ,folder name and also to remembre to chnage code folder location path)

2\. \*\*Run the script\*\*:

&nbsp;  ```cmd

&nbsp;  python folder\_locker.py

&nbsp;  ```

3\. \*\*Choose option\*\*:

&nbsp;  - `l` - Lock folder

&nbsp;  - `u` - Unlock folder

4\. \*\*Enter password\*\* when prompted



\## How It Works



1\. \*\*Lock Process\*\*:

&nbsp;  - Renames folder to `foldername\_locked\_password`

&nbsp;  - Hides the folder using `attrib +H`

&nbsp;  - Denies user access with `icacls` (requires admin)



2\. \*\*Unlock Process\*\*:

&nbsp;  - Restores access permissions

&nbsp;  - Unhides the folder

&nbsp;  - Renames back to original name



\## Important Notes



⚠️ \*\*This is for educational purposes only\*\*

\- Password is visible in folder name

\- Not suitable for sensitive data protection

\- Can be bypassed by knowledgeable users

\- Use proper encryption tools for real security needs



\## Configuration



Edit the `your\_folder` variable in the script to change target folder:

```python

your\_folder = r"C:\\Users\\user\\OneDrive\\Desktop\\TestFolder"

```



\## License



This project is for educational purposes and learning file system operations.

