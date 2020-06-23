# Drf:-
## ListAPIView:-
### for filtering results use get_queryset(self): obj = self.kwargs['url_filtering_parameter']

## RetreiveApiView or DetailAPIView:-
### uses lookup_field for filtering parameters, retreive view only return one object

# create() :- create and save in a single step, save():- first create then save

https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/

You can override get_queryset method for that purpose. As for query string parameters, you are right, request.data holds POST data, you can get query string params through request.query_params

def get_queryset(self):
    longitude = self.request.query_params.get('longitude')
    latitude= self.request.query_params.get('latitude')
    radius = self.request.query_params.get('radius')

    location = Point(longitude, latitude)

    queryset = Model.objects.filter(location__distance_lte=(location, D(m=distance))).distance(location).order_by('distance')

    return queryset

##  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)