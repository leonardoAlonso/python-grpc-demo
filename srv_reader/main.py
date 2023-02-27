
import os
import grpc
from fastapi import FastAPI

from .compiledpb2 import sale_records_pb2
from .compiledpb2 import sale_records_pb2_grpc
from .repositories.file_repository import FileRepository


app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.post('/make_grpc_request')
def make_grpc_request():
    file_repository = FileRepository("/tmp/data/100_sr.csv")
    data_readed = file_repository.read_data()

    for row in data_readed:
        with grpc.insecure_channel('srv_persistor:50051') as channel:
            stub = sale_records_pb2_grpc.SalesRecordStub(channel) # service to connect
            source = os.environ['HOSTNAME']
            request = sale_records_pb2.SalesRecordRequest(
                region = row[0],
                item_type = row[1],
                units_sold = row[2],
                unit_price = row[3],
                unit_cost = row[4],
                source = source
            )
            response = stub.SendSalesRecord(request)
            print(f'GRPC received: {response.data}')
