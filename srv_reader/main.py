
import os
import grpc
import sale_records_pb2
import sale_records_pb2_grpc

from repositories.file_repository import FileRepository



def main():

    file_repository = FileRepository("/tmp/data/10000_sr.csv")
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

if __name__ == "__main__":
    main()