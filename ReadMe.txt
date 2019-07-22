This document contains the instructions for setting up and running a cloudformation
yaml template.

Folder Structure: 
    SNStoSQStoPythonScript
		ReadMe.txt
        configurations.json
        \CloudFormation
			\Tools
				create_cf_stack.py
				lambda_to_zip.py
			lambda_code.zip
			resource_setup.yml			
        \Code
			\lambda_code
					lambda_handler.py
            RetrieveMessageFromSqs.py
	    	SendMessageToSns.py

Steps:
	1. Update the resource_setup.yml rMySqsQueuPermission Property PolicyDocument.

	2. update the configuration.json file with the correct parameters for 
	   your environment. These parameters are what the cloudformation template
	   will use to create the stack.

	3. Place lambda_code.zip in an s3 bucket within the same account/region
	   that the cloudformation stack will run.
		a. if lambda_code.zip does not exist, open the folder 
		   SNStoSQStoPythonScript as the root folder in an IDE and 
		   run the python script lambda_to_zip.py. This will create
		   the zip file of the folder "\lambda_code" and place the zip
		   file within the folder "\CloudFormation".

	4. Place the  resource_setup.yml template in an s3 bucket within the same account/region
	   that the cloudformation stack will run.

	5. Execute the script "create_cf_stack.py".

	6. Once CloudFormation stack is complete. Gather the ARN for the SNS topic 
	   along with the region where the SNS topic exists. replace the appropriate 
	   sections in the file SendMessageToSns.py and execute the script. This will
	   send a message to the SNS Topic.
	   
	7. after sending the message to SNS, gather the url from the SQS Queue that was 
	   created and the region where it exists. Replace the appropriate sections in 
	   the file RetrieveMessageFromSqs.py and execute the file. This will gather the 
	   messages from the queue.