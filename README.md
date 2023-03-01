# AWS-schedule-instance-type-lambda
This simple Lambda will change an instante type if you need to do it after hours.

1. Create AWS Lambda with Phyton last version available.
2. Deploy code.
3. Change AWS Lambda permissions by atacching the policy from this repo.
4. Be sure to change the general configuration by extending the timeout to one minute. (This is because function will wait for instance to get stopped)

![image](https://user-images.githubusercontent.com/103848038/222123223-25b6fe2a-33af-4b2e-b9d8-26f73f7b319e.png)

5. Trigger Lambda with an Eventbridge rule, scheduled as you wish, but normally you will excecute this just once e.g.: *cron(30 1 10 5 ? 2023)* (In this example, I'll do it May 5th of 2023 at 1.30am, just once)  / cron(Minutes Hours Day-of-month Month Day-of-week Year). More information: https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html

6. Save and go to sleep peacefuly.
