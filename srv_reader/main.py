
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
            request = sale_records_pb2.EmptyMessage()
            response = stub.PingSalesRecords(request)
            print(f'GRPC recived: {response.ack}')

if __name__ == "__main__":
    main()