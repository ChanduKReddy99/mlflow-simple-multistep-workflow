import mlflow


with open("artifacts01.txt", "r") as f:
    text = f.read()

new_text= 'end of stage 02'

mlflow.log_param("txt", text)
print('end of stage 02')