import os,sys
from pathlib import Path


list_of_Files = [
    #f"project_name/demo.py",
    f"Real Time Face Detection.py",
    "Face and Detection from Image.py",
    "Real Time Face and Eye Detection.py",
    "Pedestrain Detection using OpenCV.py",
    "Car Detection.py",
    "Face Detection from Image.py",
]

for filepath in list_of_Files:
    filepath = Path(filepath)
    filedir,finame = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath) or (os.path.getsize)== 0):
        with open(filepath,"w") as f:
            pass   

