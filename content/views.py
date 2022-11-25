
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status

from .models import Content
from .validate import ContentValidate


class ContentView(APIView):
    

    def get(self, request: Request) -> Response:

        contents = Content.objects.all()
        
        content_list = list()

        for content in contents:
            content_dict = model_to_dict(content)
            content_list.append(content_dict)

       
        return Response(content_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        content_is_valid = ContentValidate(**request.data)
        #entrou la no init__

        if not content_is_valid.is_valid():
            return Response(content_is_valid.errors, status.HTTP_404_NOT_FOUND)

        content = Content.objects.create(**request.data)
        content_dict = model_to_dict(content)

        return Response(content_dict, status.HTTP_201_CREATED)

class ContentModifications(APIView):
    def get(self, request: Request, content_id:int) -> Response:

        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "content not found"}, status.HTTP_404_NOT_FOUND)

        content_dict = model_to_dict(content)
        
        

        return Response(content_dict, status.HTTP_200_OK)


    def patch(self, request: Request, content_id:int) -> Response:
        
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "content not found"}, status.HTTP_404_NOT_FOUND)
        
        content.title = request.data.get("title", content.title)
        content.module = request.data.get("module", content.module)
        content.students = request.data.get("students", content.students)
        content.description = request.data.get("description", content.description)
        content.is_active = request.data.get("is_active", content.is_active) 

        content.save()
        content_dict = model_to_dict(content)

        return Response(content_dict, status.HTTP_200_OK)

    def delete(self, request: Request, content_id:int) -> Response:
        
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            return Response({"message": "content not found"}, status.HTTP_404_NOT_FOUND)

        content.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ContentParams(APIView):
    def get(self, request: Request) -> Response:
        content = request.query_params.get('title')
        contents = Content.objects.filter(title__icontains=content)
        
        content_list = list()
         
        for content in contents:
            content_dict = model_to_dict(content)
            content_list.append(content_dict)
                
        return Response(content_list, status.HTTP_200_OK)
