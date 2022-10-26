from rest_framework import serializers
from staff.models import Staff


class RecursiveField(serializers.Serializer):
    """
    Self-referential field for MPTT.
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class StaffSerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True, required=False)
    class Meta:
        model = Staff
        fields = [
            'id',
            'children',
            'position',
            'employment_date',
            'salary',
        ]

    def to_representation(self, instance):
        representation = super(StaffSerializer, self).to_representation(instance)
        representation['name'] = instance.full_name
        return representation

