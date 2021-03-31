# -*- coding: utf-8 -*-

class MapRequest:
    allowed_params = ['l', 'll', 'z']
    api_key = "40d1649f-0493-4b70-98ba-98533de7710b"
    api_url = 'https://static-maps.yandex.ru/1.x/?'

    def __init__(self):
        self.params = {'base': 123}

    def __setattr__(self, attr, value):
        if len(self.__dict__) == 0:
            self.__dict__['params'] = {}

        elif attr in MapRequest.allowed_params:
            self.__dict__['params'][f'{attr}'] = value
        # If not allowed - remember anyway
        # elif attr not in MapRequest.allowed_params:
        #     self.__dict__[f'{attr}'] = value
        else:
            raise AttributeError(attr + ' not allowed')

    def __str__(self):
        return f'Map request:'


if __name__ == '__main__':
    req = MapRequest()
    print(req)


    print(req.params)
