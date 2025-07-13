# 🗄️ Folder Locker – Python Script for Basic Folder Protection (Windows)

A simple, educational Python tool that provides basic folder locking and hiding functionality using Windows commands and file system operations.

---

 ✨ Features

- 🔐 **Rename Protection:** Appends a password to the folder name
- 👁️‍🗨️ **Hide Folder:** Uses Windows `attrib` command to make folders invisible
- 🚫 **Permission Control:** Removes access permissions with `icacls` (requires admin)
- 💻 **Simple CLI Interface:** Easy-to-use lock/unlock commands

---
 ⚙️ Requirements

- Windows OS
- Python 3.x
- Administrator privileges (for full protection)

---

 🚀 How to Use

1. **Create a folder manually**  
   Example:  
   `C:\Users\YourName\OneDrive\Desktop\TestFolder`

2. **Edit the script folder path**  
   Open `folder_locker.py` and update:

   ```python
   your_folder = r"C:\Users\YourName\OneDrive\Desktop\TestFolder"



Run the script

bash
Copy
Edit
python folder_locker.py
Choose an option:

l → Lock folder

u → Unlock folder

Enter password when prompted.

Note: Password is visible in the folder name (for demo/learning only).

📖 How It Works
🔒 Lock Process:
Renames folder to:
FolderName_locked_password

Hides the folder using:
attrib +H

Removes user permissions using:
icacls /deny Users:F

🔓 Unlock Process:
Grants user permissions back:
icacls /grant Users:F

Unhides the folder using:
attrib -H

Renames folder back to original name

⚠️ Important Notes
For learning purposes only.

Password is stored visibly in folder name and in plain text files in some versions.

Not suitable for real-world sensitive data protection.

Knowledgeable users can bypass this easily.

For actual encryption, consider tools like BitLocker, VeraCrypt, etc.

🛠️ Configuration
Update the folder path in folder_locker.py:

python
Copy
Edit
your_folder = r"C:\Users\YourName\OneDrive\Desktop\TestFolder"


📄 License
This project is provided for educational and personal learning use only.
No warranty or responsibility is provided for misuse.

   
