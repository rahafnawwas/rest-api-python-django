from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """returns a list of apiview"""
        an_apiview=[
        'uses http methods as function',
        'is similar to a trafitional',
        'is mapped manually to URLs',
        ]

        return Response({'message':'hello world!','an_apiview':an_apiview})
