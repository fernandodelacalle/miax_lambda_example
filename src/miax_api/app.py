import api_handler
import datetime


def handler(event, context):
    ah = api_handler.BMEApiHandler()
    df = ah.get_close_data("SAN")
    fecha = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    df.to_csv(f"s3://miaxlambdaout/Santander_{fecha}.csv")
