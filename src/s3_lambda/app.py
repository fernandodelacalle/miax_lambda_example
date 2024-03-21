import pandas as pd
import datetime


def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    df = pd.read_csv(f"s3://{bucket}/{key}", sep=';')
    df = df.loc[:, ["VALOR", "FECHA", "HORA", "PRECIO", "VOLUMEN"]]
    df.loc[:, "VALOR"] = df.loc[:, "VALOR"].str.rstrip()
    df = df.loc[df.loc[:, "VALOR"] == "SAN", :]

    fecha = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    df.to_csv(f"s3://miaxlambdaout/{key}_{fecha}.csv.zip", compression="zip")
