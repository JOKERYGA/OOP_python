class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('Данный запрос не может быть выполнен')

        handler_method = getattr(self, method.lower(), None)

        if handler_method is None:
            raise NotImplementedError('Метод обработки запроса не реализован')

        return handler_method(request)


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')

        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

        return "url: {}".format(request['url'])
