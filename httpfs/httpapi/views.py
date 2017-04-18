import os.path
import datetime
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework.views import APIView
from rest_framework import status


class FilesView(APIView):
    parser_classes = (FileUploadParser,)
    data_path = 'DATA/'
    metadata = {}

    def get_meta(self, filename):
        self.metadata['name'] = filename
        self.metadata['path'] = self.data_path + filename
        self.metadata['size'] = os.path.getsize(self.data_path + filename)
        self.metadata['modified'] = os.path.getmtime(self.data_path + filename)
        self.metadata['modified'] = datetime.datetime.fromtimestamp(self.metadata['modified'])
        return self.metadata


class FileGet(FilesView):
    def get(self, request, filename, format=None):
        try:
            with open(self.data_path + filename, 'rb') as f:
                response = HttpResponse(FileWrapper(f), content_type='application/file')
                response['Content-Disposition'] = 'attachment; filename="%s"' % filename
                return response
        except Exception as error:
            return Response(status.HTTP_404_NOT_FOUND)


class FilePut(FilesView):
    def put(self, request, filename, format=None):
        status_err = status.HTTP_409_CONFLICT
        status_ok = status.HTTP_201_CREATED
        try:
            up_file = request.FILES['file']

            if request.path_info.startswith('/put/'):
                if os.path.exists(self.data_path + up_file.name):
                    raise ValueError('conflict occurred')
            else:
                status_ok = status.HTTP_202_ACCEPTED
                status_err = status.HTTP_404_NOT_FOUND
                if not os.path.exists(self.data_path + up_file.name):
                    raise ValueError('not found')

            with open(self.data_path + up_file.name, 'wb+') as f:
                for chunk in up_file.chunks():
                    f.write(chunk)
            meta = self.get_meta(up_file.name)
            return Response(meta, status_ok)
        except Exception as error:
            return Response(status_err)

    def post(self, request, filename, format=None):
        return self.put(request, filename, format)


class FileMeta(FilesView):
    def get(self, request, filename, format=None):
        try:
            meta = self.get_meta(filename)
            return Response(meta, status.HTTP_200_OK) 
        except Exception as error:
            return Response(status.HTTP_404_NOT_FOUND)


class FileList(FilesView):
    def get(self, request):
        meta = {}
        for f in os.listdir(path=self.data_path):
            meta[f] = self.get_meta(f)		
        return Response(meta, status.HTTP_200_OK)


class FileRemove(FilesView):
    def put(self, request, filename, format=None):
        try:
            meta = self.get_meta(filename)
            os.remove(meta['path'])
            return Response(status.HTTP_202_ACCEPTED)
        except Exception as error:
            return Response(status.HTTP_404_NOT_FOUND)

    def post(self, request, filename, format=None):
        return self.put(request, filename, format)

