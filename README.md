
# Moving Data from Legacy to Cloud ☁️

## Why I Build 🏛️
After successfully acheiving 🚀**AWS CERTIFIED SOLUTION ARCHITECT ASSOCIATE** certification, I want to implement my knowledge in building practical projects. But where should I start?🤔 \
\
Recently, my organization has been migrating many application and databases to Google Cloud Platform (GCP). I find this as a perfect real world scenario for me to build this project where I will be migrating a SQL SERVER DB tables from LEGACY system to the AWS Cloud. 
This project is my hands-on take on an event-driven migration pipeline. It’s serverless, it’s fast, and most importantly, it’s monitored so I don't have to guess if it's working.

## What I Built🏗️ 
I built a pipeline that moves financial records from an on-premise Docker setup into a S3 bucket and stored its metadata to a modern NoSQL database on AWS. I used Docker to house SQL SERVER DB to mimic organization setup and migrated the DB to AWS. 

### The Tech Stack

- Source: SQL Server running in Docker (Legacy vibes).

- IAM: Roles for Lambda (Access Control).

- Storage: Amazon S3 (The landing zone).

- Compute: AWS Lambda (The "brain" of the operation).

- Database: Amazon DynamoDB (The metadata destination).

- Observability: CloudWatch Dashboards, Metric Filters, and SNS 

### The Architecture 📐 
<img width="981" height="591" alt="image" src="https://github.com/user-attachments/assets/e3cd1349-1643-4a99-bca6-5adba4c724ed" />
<i>draw.io for the diagram</i>

***
### How it Works (The "Deep Dive")🛠️

  ⭐ Extract and Upload: I used a Python script to pull data from the SQL container and push it to S3 via boto3.upload_file().
  
  🔫 Trigger: As soon as the file lands in S3, an s3:ObjectCreated event kicks off my Lambda.
  
  ⚙️ Process: The Lambda function uses `boto3` to get S3 metadata such as filename, filesize, creates a timestamp
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and uses dynamodb:PutItem to hold those metadata.
  
  ⚖️ Metric Filters: Scans logs for any "Error" or "Failure" keywords.
  
  ⏰ CloudWatch Alarms: These watch the filters. If something breaks, I get an **SNS** email alert immediately.
  
  📊 Dashboard: A one-stop shop to see my success rates, latency, and logs.

### Lessons Learned

- Metric Math 📖 is cool: Figuring out how to display a "dynamoDB latency" gauge on the dashboard was a fun challenge.

- Cold 🥶 Starts: Understanding how Lambda wakes up when that S3 event hits was a great deep dive into serverless behavior.

### How to Run This
- Check the /infrastructure folder for the dashboard.json if you want to replicate my monitoring setup!

- Clone the repo.

- Set up your S3 bucket triggers.

- Deploy the Lambda code in /src. 

- Upload a CSV to S3 and watch the dashboard light up. 📈

### Improvements 🦾🦾🦾
- After some research around my solution, I found that I could have added S3 ObjectKey in DynamoDB so I could quickly setup Athena for querying S3 and scale up as well.
- Add Lambda Destination SQS to capture any failure event and error trace so we can review and fix the issue.

***What's Next?***
I’m planning on implementing Infrastructure as Code (Terraform) to a AI integrated solution architecture. If you have suggestions or want to talk AWS, feel free to reach out!
