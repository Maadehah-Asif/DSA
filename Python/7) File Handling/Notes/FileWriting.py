# Create DemoFile2
f = open("demofile2.txt", "x")  # Creates the file
f.close()

# Create DemoFile3
f = open("demofile3.txt", "x")  # Creates the file
f.close()

# Open "demofile2.txt" and append content to it
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")  # Writing some content
f.close()

# Open and read "demofile2.txt" after appending
f = open("demofile2.txt", "r")
content = f.read()
f.close()

print("Content of demofile2.txt:")
print(content)

# Open "demofile3.txt" in write mode and copy content from "demofile2.txt"
f = open("demofile3.txt", "w")  # "w" will overwrite existing content
f.write(content)
f.close()

# Read and display the copied content in "demofile3.txt"
f = open("demofile3.txt", "r")
print("\nContent copied to demofile3.txt:")
print(f.read())
f.close()
