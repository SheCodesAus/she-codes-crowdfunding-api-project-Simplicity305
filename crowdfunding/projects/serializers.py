from rest_framework import serializers

from .models import Project, Pledge


class PledgeSerializer(serializers.ModelSerializer): #used model forms which interprets the model and this works similarly 
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']
        #fields = '__all__' - could have also done it this way instead of listing them all out 


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() 
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200) #NOTE was in setup - not in models setup - replaced by below in user setup
    owner = serializers.ReadOnlyField(source='owner.id') #shows a new field - owner id - in the list of project info on the main projects page
    # pledges = PledgeSerializer(many=True, read_only=True) NOTE Per Thinkific slides, this line was struck through and the be

    
    #Need to add this because otherwise we get an error that says that create isnt a thing in thr webpage without this. Serialiser doesnt know what we want to do with it even though we told it to save in views (I think)
    def create(self, validated_data):
        return Project.objects.create(**validated_data) #validated data is a dictionary that represents the data from our serialiser. ** says take everything in here and return in key values pair eg title: name of title 
    
    # METHOD FOR IMPLEMENTING PUT/UPDATE FUNCTIONALITY
    def update(self, instance, validated_data):
      	instance.title = validated_data.get('title', instance.title)
      	instance.description = validated_data.get('description', instance.description)
      	instance.goal = validated_data.get('goal', instance.goal)
      	instance.image = validated_data.get('image', instance.image)
      	instance.is_open = validated_data.get('is_open', instance.is_open)
      	instance.date_created = validated_data.get('date_created', instance.date_created)
      	instance.owner = validated_data.get('owner', instance.owner)
      	instance.save()
      	return instance
    
    
# SPLITTING THE PROJECT SERIALIZER INTO TWO
# Previously when it was just the Project serializer class, the pledges would appear under each project. By creating a new class and changing the project detail class in Views to refer to this serializer instead, we remove the pledges from showing on the projects page
class ProjectDetailSerializer(ProjectSerializer):
	pledges = PledgeSerializer(many=True, read_only=True)

        
        
