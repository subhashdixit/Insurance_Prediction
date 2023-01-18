Webapp Link:
```
https://subhashdixit-insurance-prediction-app-t93foa.streamlit.app/
```
### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```


To download your dataset

```
wget https://raw.githubusercontent.com/herbert0419/Insurance-Premium-Prediction/main/insurance.csv
```

Command to re-run the ec2 instance:
```
cd actions-runner/
./run.sh
```

Key to be used
```
AWS_ACCESS_KEY_ID= 
AWS_SECRET_ACCESS_KEY= 
AWS_REGION= 
AWS_ECR_LOGIN_URI= 
ECR_REPOSITORY_NAME=
BUCKET_NAME= 
MONGO_DB_URL= 

```

GitHub Setting:
```
* Add Runner
* Add all the keys in the secret section
```

Add Runner into EC2:
```
√ Connected to GitHub

# Runner Registration

Enter the name of the runner group to add this runner to: [press Enter for Default] 

Enter the name of runner: [press Enter for ip-172-31-32-83] self-hosted

This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
Enter any additional labels (ex. label-1,label-2): [press Enter to skip] 

√ Runner successfully added
√ Runner connection is good

```
After adding the runer into github, use all the command availabe into ec2

Install Docker into EC2
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

Deleted ECR because of charges
```
Successfully deleted repository insurance_prediction
```
