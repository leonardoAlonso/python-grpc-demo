import grpc

import sale_records_pb2
import sale_records_pb2_grpc

from concurrent import futures


class SalesRecord(sale_records_pb2_grpc.SalesRecordServicer):
    def PingSalesRecords(self, request, context):
        response = sale_records_pb2.PingSalesRecordsResponse(ack='1')
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sale_records_pb2_grpc.add_SalesRecordServicer_to_server(SalesRecord(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print("GRPC Service Persistor UP")

    server.wait_for_termination()

if __name__ == "__main__":
    main()