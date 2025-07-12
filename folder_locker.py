import os
import subprocess
import sys
 
def lock_folder(folder_path, password):
    try:
        if os.path.exists(folder_path):
            # Rename the folder
            locked_folder = folder_path + "_locked_" + password
            os.rename(folder_path, locked_folder)
            
            # Hide the folder using Windows attrib command
            subprocess.run(['attrib', '+H', locked_folder], check=True, shell=True)
            
            # Remove access permissions (requires admin)
            try:
                subprocess.run(['icacls', locked_folder, '/deny', 'Users:F'], 
                             check=True, shell=True, capture_output=True)
                print("Folder locked and access denied!")
            except subprocess.CalledProcessError:
                print("Folder locked and hidden (admin rights needed for full protection)!")
        else:
            print("Folder does not exist! Please create the folder manually first.")
    except Exception as e:
        print(f"Error: {e}")
 
def unlock_folder(folder_path, password):
    locked_folder = folder_path + "_locked_" + password
    try:
        if os.path.exists(locked_folder):
            # Restore access permissions
            try:
                subprocess.run(['icacls', locked_folder, '/grant', 'Users:F'], 
                             check=True, shell=True, capture_output=True)
            except subprocess.CalledProcessError:
                pass  # May not have been permission-locked
            
            # Unhide the folder
            subprocess.run(['attrib', '-H', locked_folder], check=True, shell=True)
            
            # Rename back to original
            os.rename(locked_folder, folder_path)
            print("Folder unlocked!")
        else:
            print("Locked folder not found or wrong password!")
    except Exception as e:
        print(f"Error: {e}")
 
# -------------------------
 
# Use OneDrive Desktop path to match your working directory
your_folder = r"C:\Users\chanu\OneDrive\Desktop\TestFolder"
 
choice = input("Lock or Unlock (l/u)? ")
 
if choice.lower() == "l":
    passcode = input("Set a password: ")
    lock_folder(your_folder, passcode)
 
elif choice.lower() == "u":
    passcode = input("Enter unlock password: ")
    unlock_folder(your_folder, passcode)
 
else:
    print("Invalid choice.")
