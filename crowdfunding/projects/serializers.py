from rest_framework import serializers

from .models import Project, Pledge


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() 
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)
    
    #Need to add this because otherwise we get an error that says that create isnt a thing in thr webpage without this. Serialiser doesnt know what we want to do with it even though we told it to save in views (I think)
    def create(self, validated_data):
        return Project.objects.create(**validated_data) #validated data is a dictionary that represents the data from our serialiser. ** says take everything in here and return in key values pair eg title: name of title 
    
class PledgeSerializer(serializers.ModelSerializer): #used model forms which interprets the model and this works similarly 
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        #fields = '__all__' - could have also done it this way instead of listing them all out 
        
        
