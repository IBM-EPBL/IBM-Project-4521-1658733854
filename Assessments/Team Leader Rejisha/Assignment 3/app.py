from flask import Flask,render_template
import ibm_boto3
from ibm_botocore.client import Config, ClientError

COS_ENDPOINT ="https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "JYwlU9YKG6_PqmieKipCKTc5-93nsBywDc9MPnxjf17m"
COS_INSTANCE_CRN= "crn:v1:bluemix:public:iam-identity::a/29fc62c631ec4081bc56bd93194cde45::"
COS_BUCKET_LOCATION="jp-tok-Storage"
cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)

app = Flask(__name__)

def get_bucket_contents(bucket_name):
    try:
        files = cos.Bucket(bucket_name).objects.all()
        edit_file = []
        for file in files:
            edit_file.append(file.key)
        return edit_file
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))




@app.route("/")

def home():
    
    return render_template("home.html",image=get_bucket_contents("ibmbucketimagess"))

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8000 ,debug=True)

