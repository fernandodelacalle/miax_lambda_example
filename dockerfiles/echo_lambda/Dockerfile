FROM public.ecr.aws/lambda/python:3.11

# Install the function's dependencies using file requirements.txt # from your project folder. 
COPY src/echo_lambda/requirements.txt  . 
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" 

# Copy function code
COPY src/echo_lambda/app.py ${LAMBDA_TASK_ROOT} 

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]