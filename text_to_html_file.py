import html
from tkinter import messagebox
def file(file_name):
    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "The file f.txt was not found!")
        return ""
def html_file(file_name,save_file_name):
    content=file(file_name)
    escape=html.escape(content)
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Text</title>
</head>
<body>
<pre>{escape}</pre>
</body>
</html>"""
    f=open(save_file_name,'w',encoding="utf-8")
    f.write(html_content)
    f.close()
    messagebox.showinfo("Success", "Data converted to html file name "+save_file_name)

#html_file()