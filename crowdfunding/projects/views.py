from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #This removes the boxes where you create a new project if you're logged out - remove this code and the box will return for - (tested).
    
    def get(self, request):
        projects = Project.objects.all() 
        #getting all the projects from projects
        serializer = ProjectSerializer(projects, many=True) #serialsiers arent smart enough so you have to tell it - hence the many =true
        return Response(serializer.data) #because we're getting the data out of the serializer so we have to ask it for the data 
    
    
    def post(self, request): #request is going to be the request object that django receives. it receives a request object and its going to do stuff with it - we're getting the payload from the request gets sent. because of the way that the api view works, it will always give you request and if you dont handle it, it wont work.abs(x)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(): #similar ish to form. someone in sydney used a walrus operator - recently introduced and usually only used in data science.
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #this added a thing in the projects page - media type and content. we want to give it some 
    
class ProjectDetail(APIView):
    

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
        #TODO Triple check this - added the permission class because last step for permissions says to do this but last step specifies project detail but first step is project list - not detail. Copying the same code from project list over to project detail. Have also implemented isownerorreadonly at project list class.
    
    def get_object(self, pk): 
        try: 
            return Project.objects.get(pk=pk) #means that pk is equal to the primary key that its been given - use pk because its not always id - could be username but has to match what we put in our url 
        #(self, monkey) pk=monkey - as an example of the relationship???
        # get the thing we specified - create a new function so we can call it in other places without repeating ourselves 
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project) #means serialise this thing in the brackets?
        return Response(serializer.data)
    #going to create an instance of a project serialiser and 

    #hes looking for a list create view in api classydrf 
    #THIS PART CONNECTS TO THE SERIALISER PLEDGE 
    
    # METHOD FOR POST
    # When viewing a specific project, there'll now be a put option. It adds boxes where you can input info. Remove this code and the box will be removed and it will just show you the 'details' of the project -(tested).
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    
class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    
    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)
        
    

