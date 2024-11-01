from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import onGoingProjects,resourceRequest , makeObjection
from .serializer import onGoingPrjSerializer, resourceRequestSerilizer ,LoginSerializer , makeObjectionSerilizer
from rest_framework import status
from django.contrib.auth import authenticate

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
#for ongoing porjects
def DeptView(request):
    # to retrive the projects based on the deptName and district
    if request.method == 'GET':
        # Get query parameters for filtering
        dept_name = request.query_params.get('DeptName')
        district = request.query_params.get('District')

        # Filter based on dept_name and district if provided
        objs = onGoingProjects.objects.all()
        
        if dept_name:
            objs = objs.filter(DeptName=dept_name)
        if district:
            objs = objs.filter(District=district)
        if not objs.exists():
            return Response({"message": "No matching records found"}, status=404)
        
        serializer = onGoingPrjSerializer(objs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
    # Handle both data and files via request.data
        data = request.data

        serializer = onGoingPrjSerializer(data=data)  # Only pass data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        else:
            return Response(serializer.errors, status=400)  # 400 Bad Request if validation fails
        

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def resourceRequests(request):

    if request.method == 'GET':
    # Retrieve and serialize all resource requests
        objs = resourceRequest.objects.all()
        serializer = resourceRequestSerilizer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = request.data
        serializer = resourceRequestSerilizer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
    
    if request.method == 'PATCH':
        try:
            # Retrieve DeptName and district from query parameters
            dept_name = request.query_params.get('DeptName')
            district = request.query_params.get('district')

            # Retrieve the object based on DeptName and district
            obj = resourceRequest.objects.get(DeptName=dept_name, district=district)
        except resourceRequest.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

        # Get data from the request body for updating
        data = request.data

        # Partially update the object
        serializer = resourceRequestSerilizer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['POST'])
def login_view(request):
    data = request.data  # Extract the request data
    serializer = LoginSerializer(data=data)
    
    if serializer.is_valid():
        # Access userId and password correctly from the data dictionary
        user_id = data.get('userId')
        password = data.get('password')
        
        user = authenticate(userId=user_id, password=password)
        # Check if user credentials match the specific values
        if user_id == "Mysmulcipality" and password == "Mysmulicality@570015":
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Invalid user ID or password'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def makeObjections(request):
    if request.method == 'POST':
        data = request.data
        serializer = makeObjectionSerilizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        objs = makeObjection.objects.all()
        serializer = makeObjectionSerilizer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)