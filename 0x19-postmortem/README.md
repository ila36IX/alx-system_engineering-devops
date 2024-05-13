# Incident report

![](https://i.imgur.com/WICOWo3.png)
## Issue Summary 

From **1:15 PM** to **3:45 PM**, we experienced downtime due to unexpectedly high traffic. This maxed out our infrastructure usage at 100%, causing our root API to respond with a 500 error code, and that made our services inaccessible. 

## Timeline

- **1:15 PM**: The system start responding with 500 error for some users, immediately our monitoring detected the failure, and sent an alert to our staff.
- **1:17 PM**: One of our engineers acknowledged the failure and start the scaling process.
- **1:20 PM**: A bug in the scaling script, leads to the execution of incorrect commands in the wrong server, which resulted to loss our data.
- **1:40 PM**: We began retrieving data from our backup servers, and redeployed the application
- **3:45 PM**: The application was up and running.

## Root Cause and Resolution

Due to the unexpected surge in traffic, our scaling script, which was still under development, was not fully ready. We needed more time to test it. However, due to the failure, one of our DevOps engineers decided that the script was ready and the odds of failure were unlikely.

After the data loss was detected, the entire team was called upon. We deployed the backup, wrote tests for the scaling script, tested it, and finally redeployed the application.
