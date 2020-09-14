from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin, HttpResponseMixin
import json
from updates.forms import UpdateModelForm
from scripts.utils import is_json

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get_object(self,id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, status=200)

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "UNknown data"}
        return self.render_to_response(data, status=403)

    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent , Please send isong JSON"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=id)
        print("rahullll", obj)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            data[key] = value
            
        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dump(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({"message": "Something"})
        return self.render_to_response(json_data)

    def delete(self, request,id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message" : "Update not found"})
            return self.render_to_response(error_data,status=404)
        deleted_ , item_deleted = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({"message" : "succesully deleted"})
            return self.render_to_response(json_data,status=200)
        error_data = json.dumps({"message" : "Could not deleted "})
        return self.render_to_response(json_data, status=400)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.filter(id__gte=1)
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "UNknown data"}
        return self.render_to_response(data, status=400)

    def put(self, request, *args, **kwargs):
        data = json.dumps({"message": "UNknown data"})
        status_code = 403
        return HttpResponse(data, status=403)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You can not delete data"})
        return HttpResponse(data, content_type='application/json')
