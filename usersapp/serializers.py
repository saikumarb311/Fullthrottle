from rest_framework import serializers
from .models import User,Activity


class ActivitySerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField(required=False)
    class Meta:
        model=Activity
        fields =[
            # 'id',
            'start_time',
            'end_time'
        ]
        read_only_fields= ('user',)
class UserSerializer(serializers.ModelSerializer):
    activitys=ActivitySerializer(many=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'real_name',
            'tz',
            'activitys'
        ]
        read_only_fields=('activitys',)
    def create(self,validated_data):
        activitys=validated_data.pop('activitys')
        user=User.objects.create(**validated_data)
        for activity in activitys:
            Activity.objects.create(**activity,user=user)
        return user
    def update(self,instance,validated_data):
        activitys=validated_data.pop("activitys")
        instance.real_name=validated_data.get("real_name",instance.real_name)
        instance.save()
        for activity in activitys:
            if "id" in activity.keys():
                if Activity.objects.filter(id=activity["id"]).exists():
                    a=Activity.objects.get(id=activity["id"])
                    a.start_time=activity.get("start_time",a.start_time)
                    a.save()
                    a.end_time=activity.get("end_time",a.end_time)
                    a.save()
                else:
                    continue
            else:
                Activity.objects.create(**activity,user=instance)
        return instance




