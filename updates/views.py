from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from . models import Update 
from django.core.serializers import serialize

# Create your views here.
def update_model_detail_view(request):
    data = {
         "count" : 1000,
         "content" : "Some new Content"
    }
    return JsonResponse(data)

def json_example(request):
    data = {
         "count" : 1000,
         "content" : "Some new Content"
    }
    json_data  =  json.dumps(data)
    return HttpResponse(json_data , content_type="application/json")


class JSONCBV(View):
    def get(self,request,*args,**kwargs):
         data = { "count" : 1000, "content" : "Some new Content" }
         return JsonResponse(data)
    
    
class JsonResponseMixin(object):
    def render_to_json_response(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context) , **response_kwargs)
    
    def get_data(self,context):
        return context
    
    
class JSONCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data = { "count" : 1000, "content" : "Some new Content" }
        return self.render_to_json_response(data)
    
    
class SerializedDetailView(View):
    def get(self,request,*args,**kwargs):
        obj = Update.objects.get(id=1)
        # print("objobj" , obj)
        # data = serialize("json" , [obj,]  , fields=('user' , 'content') )
        json_data = obj.serialize()
        return HttpResponse(json_data , content_type="application/json")
    
 
class SerializedListView(View):
    def get(self,request,*args,**kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data , content_type="application/json")