from .models import Singer, Song

from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    #songs = serializers.HyperlinkedRelatedField(
     ##   many=True,
      #  read_only=True,
      #  view_name='song-detail'  # Make sure you are using correct view name
    #)
    #songs = serializers.SlugRelatedField(
    #many=True,
    #read_only=True,
    #slug_field='title'  # or 'id' if you want ID instead of title
#)
    #songs = serializers.PrimaryKeyRelatedField(
      #  many=True,
       # read_only=True,
       # source='song_set'  # Use the related name if defined, otherwise use the default related name
    #)
    songs = serializers.HyperlinkedIdentityField(
        
        view_name='song-detail'  # Ensure this matches the URL pattern name for Song detail view
    )

    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']  # 👈 Match the field name

       

        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer',]