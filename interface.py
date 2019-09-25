from test_simple import test_simple
from flask import app,request,json,url_for,Flask
from datetime import datetime

app=Flask(__name__)

class arguments:
    def __init__(self,my_image_path,my_model_path,my_no_cuda=True):
        self.image_path = my_image_path
        self.model_name = my_model_path
        self.no_cuda=my_no_cuda

def alert(csvfile_path):
    return "Successed!"

@app.route("/api/getfeedback",methods=["GET", "POST"])
def getFeedback():
    try:
        imgName=datetime.utcnow().isoformat()
        img=request.files.get("realtimeImgs")
        path="./assets/inputs/"+imgName
        img.save(path+".jpg")
        test_simple(arguments(path+".jpg","mono+stereo_640x192"))
        return alert(path+"_disp.csv")
    except:
        return "Error"

if __name__=="__main__":
    app.run()


