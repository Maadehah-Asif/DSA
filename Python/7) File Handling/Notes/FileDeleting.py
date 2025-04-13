import os

# Check if "demofile2.txt" exists, then delete it
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
    print("demofile2.txt deleted successfully.")
else:
    print("demofile2.txt does not exist.")

# Check if "demofile3.txt" exists, then delete it
if os.path.exists("demofile3.txt"):
    os.remove("demofile3.txt")
    print("demofile3.txt deleted successfully.")
else:
    print("demofile3.txt does not exist.")
