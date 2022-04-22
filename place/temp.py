
class PlaceViewSet(ModelViewSet, ListView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'home_page']
    search_fields = ['name', 'nickname']
    permission_classes = [IsAuthenticatedOrReadOnly]

    # mapping serializer into the action
    # pagination_class = PlaceAPIListPagination


    def list(self, request, *args, **kwargs):
        queryset = Place.objects.all()
        serializer = PlaceSerializer(queryset, many=True, context={"request": request})
        new_serializer_list = []
        for index_data in range(len(serializer.data)):
            new_serializer = serializer.data[index_data].copy()
            for field in serializer.data[index_data]:

                if field not in ['id', 'name', 'description', 'images', 'rating', 'location', 'writer_user']:
                    del new_serializer[field]

                if field == 'writer_user':
                    del new_serializer[field]['id']
                    del new_serializer[field]['is_active']

            new_serializer_list.append(new_serializer)

        return Response(new_serializer_list)

    def retrieve(self, request, *args, **kwargs):
        queryset = Place.objects.filter(name=self.get_object().name)
        # print(queryset)
        serializer = PlaceSerializer(queryset, many=True, context={"request": request})

        # cto by serializer.data wytashit iz lista
        no_list_serializer = serializer.data[0]

        section = []
        owerview_section = {}

        reapet_field = ''

        new_serializer = no_list_serializer.copy()

        for field in no_list_serializer:

            if field in ['name', 'description']:
                owerview_section[field] = new_serializer[field]
                del new_serializer[field]

        new_serializer['owerview'] = owerview_section

        no_list_serializer = new_serializer.copy()


        for field in no_list_serializer:
            # if field in ['name', 'description']:
            #     owerview_section[field] = new_serializer[field]
            #     del new_serializer[field]


            if type(no_list_serializer[field]) is list and no_list_serializer[field] != [] and field not in ['category',
                                                                                                             'images']:
                print(field)
                for len_list in range(len(no_list_serializer[field])):


                    if 'name' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['name'] != '':
                        name = f'{no_list_serializer[field][len_list]["name"]}'
                        del no_list_serializer[field][len_list]["name"]
                    else:
                        name = ''

                    if 'image' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['image'] != '':
                        image = f'<img src={no_list_serializer[field][len_list]["image"]}/>'
                        del no_list_serializer[field][len_list]["image"]
                    else:
                        image = ''

                    if 'price' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['price'] != '':
                        price = f'<p>Price: {no_list_serializer[field][len_list]["price"]}</p>'
                        del no_list_serializer[field][len_list]["price"]
                    else:
                        price = ''

                    if 'comfortable' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['comfortable'] != '':
                        comfortable = f'<p>Comfortable: {no_list_serializer[field][len_list]["comfortable"]}</p>'
                        del no_list_serializer[field][len_list]["comfortable"]
                    else:
                        comfortable = ''

                    if 'how_dangerous' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'how_dangerous'] != '':
                        how_dangerous = f'<p>How Dangerous: {no_list_serializer[field][len_list]["how_dangerous"]}</p>'
                        del no_list_serializer[field][len_list]["how_dangerous"]
                    else:
                        how_dangerous = ''

                    if 'rating_danger' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'rating_danger'] != '':
                        rating_danger = f'<p>Rating Danger: {no_list_serializer[field][len_list]["rating_danger"]}</p>'
                        del no_list_serializer[field][len_list]["rating_danger"]
                    else:
                        rating_danger = ''

                    if 'continent' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'continent'] != '':
                        continent = f'<p>Continent: {no_list_serializer[field][len_list]["continent"]}</p>'
                        del no_list_serializer[field][len_list]["continent"]
                    else:
                        continent = ''

                    if 'country' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'country'] != '':
                        country = f'<p>Country: {no_list_serializer[field][len_list]["country"]}</p>'
                        del no_list_serializer[field][len_list]["country"]
                    else:
                        country = ''

                    if 'region' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'region'] != '':
                        region = f'<p>region: {no_list_serializer[field][len_list]["region"]}</p>'
                        del no_list_serializer[field][len_list]["region"]
                    else:
                        region = ''

                    if 'city' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'city'] != '':
                        city = f'<p>City: {no_list_serializer[field][len_list]["city"]}</p>'
                        del no_list_serializer[field][len_list]["city"]
                    else:
                        city = ''

                    if 'latitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'latitude'] != '':
                        latitude = f'<p>Latitude: {no_list_serializer[field][len_list]["latitude"]}</p>'
                        del no_list_serializer[field][len_list]["latitude"]
                    else:
                        latitude = ''

                    if 'longitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'longitude'] != '':
                        longitude = f'<p>Longitude: {no_list_serializer[field][len_list]["longitude"]}</p>'
                        del no_list_serializer[field][len_list]["longitude"]
                    else:
                        longitude = ''

                    if 'nearest_place' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'nearest_place'] != '':
                        nearest_place = f'<p>nearest_place: {no_list_serializer[field][len_list]["nearest_place"]}</p>'
                        del no_list_serializer[field][len_list]["nearest_place"]
                    else:
                        nearest_place = ''


                    if field in ['flora_fauna']:
                        new_serializer[field][len_list]['display_type'] = 'grid'
                        if reapet_field != field:
                            # print('type: ', len(no_list_serializer[field]))
                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
                            else:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
                                del no_list_serializer[field][len_list]['description']
                            del no_list_serializer[field][len_list]['id']

                            no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
                            no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
                            no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")

                            reapet_field = field
                            section.append(no_list_serializer[field][len_list])

                        else:

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
                            else:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})
                    else:
                        if reapet_field != field:
                            # print('type: ', len(no_list_serializer[field]))

                            new_serializer[field][len_list]['display_type'] = 'drop_down'

                            if field in ['location', 'practical_information', 'interesting_fact']:
                                new_serializer[field][len_list]['display_type'] = 'simple'

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
                            else:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
                                del no_list_serializer[field][len_list]['description']
                            del no_list_serializer[field][len_list]['id']

                            no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
                            no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
                            no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")

                            reapet_field = field
                            section.append(no_list_serializer[field][len_list])

                        else:

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
                            else:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})

                del new_serializer[field]
        # new_serializer['owerview'] = owerview_section

        new_serializer['sections'] = section


        return Response(new_serializer)

    @action(detail=False, methods=["get"])
    def plus_place(self, request):
        # queryset = Place.objects.all()
        # serializer = PlaceSerializer(queryset, many=True)
        # return Response(serializer.data)
        return Response(plus_place)

    def perform_create(self, serializer):
        address = serializer.initial_data["name"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print('pnt_create: ', pnt)
        serializer.save(location=pnt)

    def perform_update(self, serializer):
        address = serializer.initial_data["address"]
        g = geolocator.geocode(address)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print('pnt_update: ', pnt)
        serializer.save(location=pnt)
