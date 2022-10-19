// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             (unknown)
// source: gempellm/logistic_parcel_api/v1/logistic_parcel_api.proto

package logistic_parcel_api

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// LogisticParcelApiServiceClient is the client API for LogisticParcelApiService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type LogisticParcelApiServiceClient interface {
	// DescribeParcelV1 - Describe a parcel
	DescribeParcelV1(ctx context.Context, in *DescribeParcelV1Request, opts ...grpc.CallOption) (*DescribeParcelV1Response, error)
}

type logisticParcelApiServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewLogisticParcelApiServiceClient(cc grpc.ClientConnInterface) LogisticParcelApiServiceClient {
	return &logisticParcelApiServiceClient{cc}
}

func (c *logisticParcelApiServiceClient) DescribeParcelV1(ctx context.Context, in *DescribeParcelV1Request, opts ...grpc.CallOption) (*DescribeParcelV1Response, error) {
	out := new(DescribeParcelV1Response)
	err := c.cc.Invoke(ctx, "/gempellm.logistic_parcel_api.v1.LogisticParcelApiService/DescribeParcelV1", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// LogisticParcelApiServiceServer is the server API for LogisticParcelApiService service.
// All implementations must embed UnimplementedLogisticParcelApiServiceServer
// for forward compatibility
type LogisticParcelApiServiceServer interface {
	// DescribeParcelV1 - Describe a parcel
	DescribeParcelV1(context.Context, *DescribeParcelV1Request) (*DescribeParcelV1Response, error)
	mustEmbedUnimplementedLogisticParcelApiServiceServer()
}

// UnimplementedLogisticParcelApiServiceServer must be embedded to have forward compatible implementations.
type UnimplementedLogisticParcelApiServiceServer struct {
}

func (UnimplementedLogisticParcelApiServiceServer) DescribeParcelV1(context.Context, *DescribeParcelV1Request) (*DescribeParcelV1Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DescribeParcelV1 not implemented")
}
func (UnimplementedLogisticParcelApiServiceServer) mustEmbedUnimplementedLogisticParcelApiServiceServer() {
}

// UnsafeLogisticParcelApiServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to LogisticParcelApiServiceServer will
// result in compilation errors.
type UnsafeLogisticParcelApiServiceServer interface {
	mustEmbedUnimplementedLogisticParcelApiServiceServer()
}

func RegisterLogisticParcelApiServiceServer(s grpc.ServiceRegistrar, srv LogisticParcelApiServiceServer) {
	s.RegisterService(&LogisticParcelApiService_ServiceDesc, srv)
}

func _LogisticParcelApiService_DescribeParcelV1_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DescribeParcelV1Request)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(LogisticParcelApiServiceServer).DescribeParcelV1(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/gempellm.logistic_parcel_api.v1.LogisticParcelApiService/DescribeParcelV1",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(LogisticParcelApiServiceServer).DescribeParcelV1(ctx, req.(*DescribeParcelV1Request))
	}
	return interceptor(ctx, in, info, handler)
}

// LogisticParcelApiService_ServiceDesc is the grpc.ServiceDesc for LogisticParcelApiService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var LogisticParcelApiService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "gempellm.logistic_parcel_api.v1.LogisticParcelApiService",
	HandlerType: (*LogisticParcelApiServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "DescribeParcelV1",
			Handler:    _LogisticParcelApiService_DescribeParcelV1_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "gempellm/logistic_parcel_api/v1/logistic_parcel_api.proto",
}