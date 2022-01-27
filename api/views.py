from django.http import Http404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Study
from api.serializers import StudySerializer


class StudyView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Study.objects.all()
        studies = StudySerializer(data=snippets, many=True)
        studies.is_valid()
        return Response(studies.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        study = Study()
        study.urgency_level = data["urgency_level"]
        study.body_part = data["body_part"]
        study.description = data["description"]
        study.type = data["type"]
        study.save()
        study_result = {
            "urgency_level": study.urgency_level,
            "body_part": study.body_part,
            "description": study.description,
            "type": study.type
        }
        return Response(study_result, status=status.HTTP_202_ACCEPTED)


class StudyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Study.objects.get(pk=pk)
        except Study.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = StudySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        study = self.get_object(pk)
        serializer = StudySerializer(study, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
