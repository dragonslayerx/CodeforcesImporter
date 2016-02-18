class Urlbuilder:

    def __init__(self, base_url, method):
        self.base_url = ''
        self.method = ''
        self.param_args = {}

        # call setters for base_url and method
        self.set_base_url(base_url)
        self.set_method(method)

    def set_base_url(self, base_url):
        self.base_url = base_url
        return self

    def set_method(self, method):
        self.method = method
        return self

    def add_param(self, param, arg):
        self.param_args[param] = arg
        return self

    def get_url(self):
        url = self.base_url + '/' + self.method
        param_list = []

        for key in self.param_args:
            param_list.append((key, self.param_args[key]))

        if len(param_list) > 0:
            url += '?'
            for i in range(0, len(param_list)):
                url = url + param_list[i][0] + '=' + param_list[i][1]
                if i+1 < len(param_list):
                    url += '&'

        return url